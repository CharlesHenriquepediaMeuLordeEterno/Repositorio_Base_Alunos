'''
x=1
while x<=3:
    print(x)
    x = x + 1

x=50
while x<=100:
    print(x)
    x = x + 1

x=1
while x<=100:
    print(x)
    x = x + 1


def contagem_regressiva():
    x = 10
    while x >= 0:
        print(x)
        x = x - 1
    print("Fogo!")
contagem_regressiva()

def numeros_pares():
    
    fim=int(input("Digite o último número a imprimir: "))
    x = 0
    while x <= fim:
        if x % 2 == 0:
            print(x)
        x = x + 1
numeros_pares()

def numeros_ímpares():
    
    fim=int(input("Digite o último número a imprimir: "))
    x = 0
    while x <= fim:
        if x % 2 == 1:
            print(x)
        x = x + 1
numeros_ímpares()

def arvore_de_natal():
    linha = 1
    while linha <=10:
        coluna = 1
        while coluna <= linha:
            coluna = coluna + 1
            if linha %2 == 1:
                print('👹', end="")
            else:
                print('👿', end="")
        print()
        linha = linha + 1
arvore_de_natal()
'''