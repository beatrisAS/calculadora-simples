import subprocess
import sys


# Função auxiliar - use em todos os testes abaixo!
# As entradas devem seguir a ordem pedida pelo programa:
# primeiro número, segundo número e operador.
def preparar_variaveis(lista_entradas):
    # Prepara as variáveis
    texto_entrada = '\n'.join(lista_entradas)
    dados_entrada = texto_entrada.encode('utf-8')

    # Obtém a saída real a partir das entradas
    # sys.executable usa o mesmo Python do pytest; -X utf8 evita problemas de acentos no Windows
    resultado = subprocess.run(
        [sys.executable, '-X', 'utf8', 'main.py'],
        input=dados_entrada,
        stdout=subprocess.PIPE
    )
    saida_bytes = resultado.stdout.strip()
    saida_texto = saida_bytes.decode("utf-8")

    # O Windows gera CR (\r\n), então removemos
    saida_real = saida_texto.replace('\r\n', '\n')

    return saida_real


# Confere o VALOR do resultado, e não a forma como ele foi escrito.
# Assim, "10" e "10.0" são aceitos, e "3.33" e "3.3333333" também (tolerância de 0.01).
# O texto das perguntas feitas com input() fica na mesma linha do resultado,
# então o valor é a última palavra da última linha da saída.
def verificar_resultado(saida_real, valor_esperado):
    ultima_linha = saida_real.splitlines()[-1]
    texto_do_valor = ultima_linha.split()[-1]
    assert abs(float(texto_do_valor) - valor_esperado) <= 0.01


# Confere se a ÚLTIMA linha da saída termina exatamente com a mensagem de erro esperada.
def verificar_erro(saida_real, mensagem_esperada):
    ultima_linha = saida_real.splitlines()[-1]
    assert ultima_linha.endswith(mensagem_esperada)


# Teste 1 - soma
def test_soma():
    saida_real = preparar_variaveis(['8', '2', '+'])
    verificar_resultado(saida_real, 10)


# Teste 2 - soma com decimais
def test_soma_decimais():
    saida_real = preparar_variaveis(['1.5', '2.25', '+'])
    verificar_resultado(saida_real, 3.75)


# Teste 3 - soma de 0.1 + 0.2 (o computador pode mostrar 0.30000000000000004)
def test_soma_decimais_pequenos():
    saida_real = preparar_variaveis(['0.1', '0.2', '+'])
    verificar_resultado(saida_real, 0.3)


# Teste 4 - subtração
def test_subtracao():
    saida_real = preparar_variaveis(['10', '4', '-'])
    verificar_resultado(saida_real, 6)


# Teste 5 - subtração com resultado negativo
def test_subtracao_negativa():
    saida_real = preparar_variaveis(['3', '5', '-'])
    verificar_resultado(saida_real, -2)


# Teste 6 - resultado zero
def test_resultado_zero():
    saida_real = preparar_variaveis(['5', '5', '-'])
    verificar_resultado(saida_real, 0)


# Teste 7 - multiplicação
def test_multiplicacao():
    saida_real = preparar_variaveis(['6', '7', '*'])
    verificar_resultado(saida_real, 42)


# Teste 8 - multiplicação com decimal
def test_multiplicacao_decimal():
    saida_real = preparar_variaveis(['1.5', '2', '*'])
    verificar_resultado(saida_real, 3)


# Teste 9 - divisão exata
def test_divisao_exata():
    saida_real = preparar_variaveis(['20', '5', '/'])
    verificar_resultado(saida_real, 4)


# Teste 10 - divisão com resultado decimal
def test_divisao_decimal():
    saida_real = preparar_variaveis(['7', '2', '/'])
    verificar_resultado(saida_real, 3.5)


# Teste 11 - divisão com muitas casas decimais (3.3333...)
def test_divisao_dizima():
    saida_real = preparar_variaveis(['10', '3', '/'])
    verificar_resultado(saida_real, 3.33)


# Teste 12 - divisão por zero
def test_divisao_por_zero():
    saida_real = preparar_variaveis(['10', '0', '/'])
    verificar_erro(saida_real, 'Não é possível dividir por zero')


# Teste 13 - operador inválido
def test_operador_invalido():
    saida_real = preparar_variaveis(['5', '3', '%'])
    verificar_erro(saida_real, 'Operador inválido')


# Teste 14 - o enunciado pede uma solução sem funções criadas por você
def test_sem_funcoes_proprias():
    with open('main.py', encoding='utf-8') as arquivo:
        codigo = arquivo.read()

    assert 'def ' not in codigo
    assert 'lambda' not in codigo
