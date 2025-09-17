'''
"""massa = float( input() )
velocidade = float( input() )
"""
# fórmula de energia cinética: EC = m x v / 2

# um comentário
# outro comentário
# mais outro comentário

"""
um comentário
outro comentário
"""

def dizer_ola(nome_usuario = "Mundo"):
     print("Olá", nome_usuario)

dizer_ola("Rodrigo")
dizer_ola()

dizer_ola("Gato")

dizer_ola(77/7)



numero = int(input("Insira um número: "))

saudacao = numero * 7
print(saudacao)



numero = 7

def apresentar_numero():
    global numero
    print (numero)
    numero = 11
    print(numero)

apresentar_numero()
print(numero)
'''


def quadrado(area):
    resultado = area ** 2
    return resultado
print (quadrado(4))

def salario(valor):
    resultado = valor + valor * 0.15
    return resultado
print(salario(1500))

def triangulo(base, altura):
    resultado = base * altura / 2
    return resultado
print(triangulo(4,2))

def fahrenheit(C):
    resultado = (9*C+160) /5.
    return resultado
print(fahrenheit(100))

def valores(x, y):
    temp = x
    x = y
    y = temp
    print(x, y)

print(valores(7, 11))

def volume(comprimento, largura, altura):
    resultado = comprimento * largura * altura
    return resultado

print("paralelepípedo"(10, 7, 15))



    
