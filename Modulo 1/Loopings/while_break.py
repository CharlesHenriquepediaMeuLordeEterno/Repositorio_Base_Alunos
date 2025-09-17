'''
L=[]

while True:

    n = int(input("Digite um número (0 sai): "))

    if n == 0:

        break
    L.append(n)

x=0

while x <len(L):

    print(L[x])

    x = x + 1
'''

L=[]
while True:

    n = (input("Digite uma palavra (Pare sai): "))

    if n == "Pare":

        break
    L.append(n)

x=0
while x <len(L):

       print(L)

