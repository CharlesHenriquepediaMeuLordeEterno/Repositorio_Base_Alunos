try:
    divisão = 10 / 0
   #print(divisão)
except:
   # print('''Não foi
   # possível realizar
    #essa operação!''') 
     
     
    #def divide(x,y):
        #try:
            #result = x/y
        #except ZeroDivisionError:
            #print("Por favor, não utilize zeros!")
        #except:
            #print("\033[91m Algo deu errado... ")
       # else:
            #print(f"Seu resultado é: {result}")
        #finally:
            #print("\033[92m Vamos de novo?")
    #divide(13,0)

    def match_case():
        import random
        value = random.randint(0, 2)

        match value:
            case 0:
                print("Zero!")
            case 1:
                print("Um!")
            case 2:
                print("Dois!")
            case _:
                print("exceção")
match_case()
