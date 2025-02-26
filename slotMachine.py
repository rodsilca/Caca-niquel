import random

MAX_LINHAS =3
MAX_APOSTA = 100
MIN_APOSTA = 1

LINHAS =3
COLUNAS =3

contagemSimbolos = {"A": 2,"B": 4, "C": 6, "D": 8}
contagemSimbolosValor = {"A": 5,"B": 4, "C": 3, "D": 2}

def checarGanhos(colunas,linhas, aposta,valores):
    ganhos = 0
    linhasGanhas = []
    for linha in range(linhas):
        simbolo = colunas[0][linha]
        for coluna in colunas:
            simbCheck = coluna[linha]
            if simbolo != simbCheck:
                break
        else:
            ganhos += valores[simbolo] * aposta
            linhasGanhas.append(linha+1)

    return ganhos,linhasGanhas

def getGiroRoleta(linhas,colunas,simbolos):
    todosSimbolos = []
    for simbolo,valor in simbolos.items():
        for _ in range(valor):
            todosSimbolos.append(simbolo)

    colunasRoleta = []
    for _ in range(colunas):
        coluna = []
        simbsAtuais = todosSimbolos[:]
        for _ in range(linhas):
            val = random.choice(simbsAtuais)
            simbsAtuais.remove(val)
            coluna.append(val)

        colunasRoleta.append(coluna)

    return colunasRoleta

def imprimir(colunas):
    for linha in range(len(colunas[0])):
        for i, coluna in enumerate(colunas):
            if i != len(colunas)-1:
                print(coluna[linha], end=" | ")
            else:
                print(coluna[linha],end="")
        print()

def depositar():
    while True:
        quantia = input("Quanto voce gostaria de depositar? R$")
        if quantia.isdigit():
            quantia = int(quantia)
            if quantia >0:
                break
            else:
                print("A quantidade deve ser maior que 0")
        else:
            print("Por favor insira um numero válido")
    return quantia

def getNumeroLinhas():
    while True:
        linhas = input(f"Em quantas linhas voce gostaria de apostar?(1 - {MAX_LINHAS})")
        if linhas.isdigit():
            linhas = int(linhas)
            if MAX_LINHAS >= linhas >=0:
                break
            else:
                print("Insira uma quantidade válida de linhas (1 - 3)")
        else:
            print("Por favor insira um numero válido")
    return linhas

def getAposta():
    while True:
        quantia = input("Quanto voce gostaria de apostar em cada linha? R$")
        if quantia.isdigit():
            quantia = int(quantia)
            if MAX_APOSTA >= quantia >=MIN_APOSTA :
                break
            else:
                print(f"A quantia deve ser maior que R${MIN_APOSTA} - R${MAX_APOSTA}")
        else:
            print("Por favor insira um numero válido")
    return quantia

def jogada(saldo):
    linhas = getNumeroLinhas()
    while True:
        aposta = getAposta()
        apostaTotal = aposta * linhas

        if apostaTotal > saldo:
            print(f"Voce nao possui saldo suficiente para a aposta, seu saldo atual é R${saldo}")
        else:
            break

    print(f"Voce esta apostando R${aposta} em {linhas} linhas. Aposta total de R${apostaTotal}")

    slots = getGiroRoleta(LINHAS, COLUNAS, contagemSimbolos)
    imprimir(slots)
    ganhos, linhasGanhas = checarGanhos(slots, linhas, aposta, contagemSimbolosValor)
    print(f"VOCE GANHOU: R${ganhos}")
    print(f"VOCE GANHOU NAS LINHAS: ", *linhasGanhas)
    return ganhos - apostaTotal

def main():
    saldo = depositar()
    while True:
        print(f"Saldo atual: R${saldo}")
        rodar = input("Pressione Enter para jogar (s para sair) ").lower()
        if rodar == "s":
            break
        saldo +=jogada(saldo)
    print(f"Voce saiu com R${saldo}")

main()