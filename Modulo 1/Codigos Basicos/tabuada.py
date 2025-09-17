'''
n=int(input("Tabuada do: "))
x = 1
n=int(input("Número para multiplicar: "))
while x<=10:
    x = x + 1
    y = x
    print(n,"x", x , "=" , x*n)


def tabuada():

    n=int(input("Tabuada do: "))
    fim=int(input("Número final para multiplicar: "))
    x = 1
    while x <= fim:
        print(n,"x", x , "=" , x*n)
        x = x + 1
tabuada()
'''

s = 0
c = 0
while True:
    v=int(input("Digite um número a somar ou 0 para sair: "))
    
    if v==0:
        break
    s += v
    c += 1

if c > 0:
    media = s / c
    print("Soma: ", s)
    print("Quantidade de valores", c)
    print("Média dos valores: ", media)
else:
    print("Nenhum número informado")


    

