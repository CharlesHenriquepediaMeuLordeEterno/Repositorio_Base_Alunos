tupla = ("03/05/2009", "Caxias do Sul", "058.xxx.xxx-30")
tupla

L=[5,9,13,21,36,45,54,61,72,81]
for x, e in enumerate(L):
    print("[%d] %d" % (x,e))    
    print("[%d] - %d = %d " % (x,e, x-e)) #Subtração
    print("[%d] + %d = %d " % (x,e, x+e)) #Adição
    print("[%d] X %d = %d " % (x, e, x*e)) #Multiplicação
    print("[%d / %d = %f " % (x,e, x/e)) #Divisão

    