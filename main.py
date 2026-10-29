# Avaliação de laboratório Python: Calculadora Básica

# ---------------------------------------------------------------
# Cores (as mesmas do cores.py, copiadas aqui para este arquivo
# funcionar sozinho)
# ---------------------------------------------------------------
RESET = "\033[0m"
ESTILO_NEGRITO = "\033[1m"

FRENTE_PRETO = "\033[30m"
FRENTE_CINZA = "\033[90m"
FRENTE_BRANCO_CLARO = "\033[97m"

FUNDO_AZUL = "\033[44m"
FUNDO_CINZA = "\033[100m"
FUNDO_VERMELHO_CLARO = "\033[101m"
FUNDO_VERDE_CLARO = "\033[102m"
FUNDO_AMARELO_CLARO = "\033[103m"
FUNDO_MAGENTA_CLARO = "\033[105m"
FUNDO_CIANO_CLARO = "\033[106m"

LARGURA = 36

# ---------------------------------------------------------------
# Cabeçalho: barra de título e teclas da calculadora
# ---------------------------------------------------------------
tecla_soma = FUNDO_VERDE_CLARO + FRENTE_PRETO + ESTILO_NEGRITO + "  +  " + RESET
tecla_menos = FUNDO_AMARELO_CLARO + FRENTE_PRETO + ESTILO_NEGRITO + "  -  " + RESET
tecla_vezes = FUNDO_MAGENTA_CLARO + FRENTE_PRETO + ESTILO_NEGRITO + "  *  " + RESET
tecla_divide = FUNDO_CIANO_CLARO + FRENTE_PRETO + ESTILO_NEGRITO + "  /  " + RESET

legenda = "soma".center(5) + "  " + "menos".center(5) + "  " + "vezes".center(5) + "  " + "div".center(5)

print()
print("  " + FUNDO_AZUL + FRENTE_BRANCO_CLARO + ESTILO_NEGRITO + "CALCULADORA".center(LARGURA) + RESET)
print("  " + FRENTE_CINZA + "calculadora de bolso".center(LARGURA) + RESET)
print()
print("  " + " " * 5 + tecla_soma + "  " + tecla_menos + "  " + tecla_vezes + "  " + tecla_divide)
print("  " + " " * 5 + FRENTE_CINZA + legenda + RESET)
print()

# ---------------------------------------------------------------
# Entrada de dados (nesta ordem: número, número, operador)
# ---------------------------------------------------------------
texto1 = input("  " + FUNDO_AZUL + FRENTE_BRANCO_CLARO + " 1 " + RESET + " Primeiro número: ")
texto2 = input("  " + FUNDO_AZUL + FRENTE_BRANCO_CLARO + " 2 " + RESET + " Segundo número: ")
operador = input("  " + FUNDO_AZUL + FRENTE_BRANCO_CLARO + " 3 " + RESET + " Operador (+ - * /): ").strip()

numero1 = float(texto1)
numero2 = float(texto2)

# ---------------------------------------------------------------
# Cálculo
# ---------------------------------------------------------------
resultado = 0
mensagem_erro = ""

if operador == "+":
    resultado = numero1 + numero2
elif operador == "-":
    resultado = numero1 - numero2
elif operador == "*":
    resultado = numero1 * numero2
elif operador == "/":
    if numero2 == 0:
        mensagem_erro = "Não é possível dividir por zero"
    else:
        resultado = numero1 / numero2
else:
    mensagem_erro = "Operador inválido"

# ---------------------------------------------------------------
# Saída: o resultado (ou o erro) é a ÚLTIMA coisa exibida
# ---------------------------------------------------------------
print()

if mensagem_erro != "":
    print("  " + FUNDO_VERMELHO_CLARO + FRENTE_PRETO + ESTILO_NEGRITO + " ✖ ERRO " + RESET + " " + mensagem_erro)
else:
    resultado = round(resultado, 2)       # no máximo 2 casas decimais
    if resultado == int(resultado):
        resultado = int(resultado)        # 10.0 vira 10

    expressao = texto1 + " " + operador + " " + texto2

    # Visor da calculadora (faixa cinza com a conta alinhada à direita)
    print("  " + FUNDO_CINZA + " " * LARGURA + RESET)
    print("  " + FUNDO_CINZA + FRENTE_BRANCO_CLARO + expressao.rjust(LARGURA - 2) + "  " + RESET)
    print("  " + FUNDO_CINZA + " " * LARGURA + RESET)
    print()
    print("  " + FUNDO_VERDE_CLARO + FRENTE_PRETO + ESTILO_NEGRITO + " ✔ RESULTADO " + RESET + " " + str(resultado))
