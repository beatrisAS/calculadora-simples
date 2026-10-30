# ---------------------------------------------------------------
# Cores e Design 
# ---------------------------------------------------------------
RESET = "\033[0m"
ESTILO_NEGRITO = "\033[1m"
FRENTE_PRETO = "\033[30m"
FRENTE_CINZA = "\033[90m"
FRENTE_BRANCO = "\033[97m"
FRENTE_AMARELO = "\033[93m"
FRENTE_CIANO = "\033[96m"

FUNDO_ROXO = "\033[48;5;55m"
FUNDO_CINZA_ESCURO = "\033[48;5;236m"
FUNDO_VERDE = "\033[42m"
FUNDO_VERMELHO = "\033[41m"

LARGURA = 50

# ---------------------------------------------------------------
# As 4 Funções Obrigatórias do Projeto 5
# ---------------------------------------------------------------
def somarmultiplosnumeros(numeros):
    soma = 0
    for numero in numeros:
        soma = soma + numero
    return soma

def multiplicarmultiplosnumeros(numeros):
    produto = 1
    for numero in numeros:
        produto = produto * numero
    return produto

def ehinteiro(numero):
    if type(numero) == str:
        return False
    if int(numero) == numero:
        return True
    else:
        return False

def ehpar(numero):
    if ehinteiro(numero) == True:
        if numero % 2 == 0:
            return True
        else:
            return False
    else:
        return False

# ---------------------------------------------------------------
# Saudação e Mascote
# ---------------------------------------------------------------
print()
print("  " + FUNDO_ROXO + FRENTE_BRANCO + ESTILO_NEGRITO + "  CALCULADORA  ".center(LARGURA) + RESET)
print("  " + FUNDO_CINZA_ESCURO + FRENTE_CINZA + "Construa sua conta passo a passo".center(LARGURA) + RESET)

print(f"""
    {FRENTE_AMARELO} /\\_/\\ {RESET}
    {FRENTE_AMARELO}( o.o ){RESET}  {ESTILO_NEGRITO}Olá! Eu sou o CalCat!{RESET}
    {FRENTE_AMARELO} > ^ < {RESET}  {FRENTE_CINZA}Vamos montar uma conta juntos?{RESET}
""")

# ---------------------------------------------------------------
# Entrada de Dados Passo a Passo
# ---------------------------------------------------------------
partes = []

# Pede o primeiro número
texto_num = input(f"  {FRENTE_CIANO}➜{RESET} {ESTILO_NEGRITO}Digite o 1º número:{RESET} ")
partes.append(float(texto_num))

while True:
    print(f"  {FRENTE_CINZA}-------------------------------------------------{RESET}")
    op = input(f"  {FRENTE_CIANO}➜{RESET} {ESTILO_NEGRITO}Operador{RESET} (+, -, *, /) ou {FRENTE_AMARELO}'=' para calcular:{RESET} ").strip()
    
    if op == "=":
        break
    elif op == "+" or op == "-" or op == "*" or op == "/":
        partes.append(op)
        texto_num = input(f"  {FRENTE_CIANO}➜{RESET} {ESTILO_NEGRITO}Digite o próximo número:{RESET} ")
        partes.append(float(texto_num))
    else:
        print(f"  {FUNDO_VERMELHO}{FRENTE_PRETO} ERRO {RESET} Operador inválido. Tente novamente.")

# ---------------------------------------------------------------
# Processamento Matemático (Regra BODMAS)
# ---------------------------------------------------------------
mensagem_erro = ""

# Guarda a conta original em texto para mostrar no visor final
conta_texto = ""
for item in partes:
    if type(item) != str and ehinteiro(item) == True:
        conta_texto = conta_texto + str(int(item)) + " "
    else:
        conta_texto = conta_texto + str(item) + " "

# Passo 1: Resolve todas as Multiplicações e Divisões primeiro
i = 0
while i < len(partes):
    if partes[i] == "*":
        resultado = multiplicarmultiplosnumeros([partes[i-1], partes[i+1]])
        partes[i-1] = resultado
        partes.pop(i)
        partes.pop(i)
        i = i - 1
    elif partes[i] == "/":
        if partes[i+1] == 0:
            mensagem_erro = "Não é possível dividir por zero"
            break
        resultado = partes[i-1] / partes[i+1]
        partes[i-1] = resultado
        partes.pop(i)
        partes.pop(i)
        i = i - 1
    i = i + 1

# Passo 2: Resolve todas as Somas e Subtrações
if mensagem_erro == "":
    i = 0
    while i < len(partes):
        if partes[i] == "+":
            resultado = somarmultiplosnumeros([partes[i-1], partes[i+1]])
            partes[i-1] = resultado
            partes.pop(i)
            partes.pop(i)
            i = i - 1
        elif partes[i] == "-":
            resultado = partes[i-1] - partes[i+1]
            partes[i-1] = resultado
            partes.pop(i)
            partes.pop(i)
            i = i - 1
        i = i + 1

# ---------------------------------------------------------------
# Saída Final e Análise
# ---------------------------------------------------------------
print("\n")
if mensagem_erro != "":
    print("  " + FUNDO_VERMELHO + FRENTE_PRETO + ESTILO_NEGRITO + " ✖ ERRO " + RESET + " " + mensagem_erro)
else:
    resultado_final = partes[0]
    
    if ehinteiro(resultado_final) == True:
        resultado_final = int(resultado_final)

    print("  " + FUNDO_CINZA_ESCURO + " " * LARGURA + RESET)
    print("  " + FUNDO_CINZA_ESCURO + FRENTE_BRANCO + conta_texto.strip().rjust(LARGURA - 2) + "  " + RESET)
    print("  " + FUNDO_CINZA_ESCURO + " " * LARGURA + RESET)
    print("  " + FUNDO_VERDE + FRENTE_PRETO + ESTILO_NEGRITO + " ✔ RESULTADO FINAL " + RESET + " " + str(resultado_final))
    print()
    
    print(f"  {FRENTE_AMARELO}CalCat analisou o seu resultado:{RESET}")
    if ehpar(resultado_final) == True:
        print(f"  {FRENTE_CIANO}•{RESET} É um número Par.")
    else:
        print(f"  {FRENTE_CIANO}•{RESET} Não é um número Par.")
        
    if ehinteiro(resultado_final) == True:
        print(f"  {FRENTE_CIANO}•{RESET} É um número Inteiro.")
    else:
        print(f"  {FRENTE_CIANO}•{RESET} É um número Decimal.")
print()