#L = [8,9,15]
#for Marcos in L:
    #print(Marcos)

#L=["cyberpunk 2077", "elden ring", "bordelands","terraria", "palword", "daed cells", "fifa 25", "dragon ball xenoverse", "castle crashers", "devil may cry"]
#for s in L:
    #for letra in s:
        #print(letra)

def exiba_o_maior():
    L=[1,7,2,4]
    máximo=L[0]
    for e in L:
        if e > máximo:
            máximo = e
    print(máximo)
#exiba_o_maior()

def exiba_o_menor():
    L=[1,7,2,4]
    menor=L[0]
    for e in L:
        if e < menor:
            menor = e
    print(menor)
#exiba_o_menor()

def range_exemplo():
    for v in range(10):
        print(v)
#range_exemplo()

def range_inicio_e_fim():
    for v in range (5, 8):
        print (v)
#range_inicio_e_fim()

def range_saltos():
    for t in range(0,50000,350):
        print(t, end=" ")
#range_saltos()

nome = "Marcos"
idade = 16
grana = 22.17
print("%s tem %d anos e R$%5.2f no bolso. " % (nome, idade, grana))

