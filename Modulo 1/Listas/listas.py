import math
def equação():
    A = float(input("Insira o valor de A: "))
    B = float(input("Insira o valor de B: "))
    C = float(input("Insira o valor de C: "))
    Delta = B**2 - 4 * A * C
    if Delta > 0:
        x = (-B + math.sqrt(Delta)) / 2 * A
        y = (-B - math.sqrt(Delta)) / 2 * A
        raiz_quadrada = math.sqrt(Delta)
        print("A raiz quadrada5",
        "é", raiz_quadrada)
        print("O resultado é " ,x, y)
    else:
        print('''Essa equação não possui
              raízes reais''')
#equação()

import random

numero_aleatorio = random.randint(0, 10)
print(numero_aleatorio)

jogadores = [ 'Messi', 'Neymar', 'Cristiano Ronaldo', 'Mbappé', 'Ibrahimovic', 'Griezmann', 'Suárez', 'Lewandowski', 'Veiga', 'Pelé', 'Robinho', 'Daniel Alves']
print(random.choice(jogadores))

import time

print(time.asctime())

import turtle

turtle.circle(250)
turtle.getscreen()._root.mainloop()


import this