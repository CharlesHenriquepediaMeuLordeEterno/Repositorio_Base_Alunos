"""
valor_total = 0
raças = ['pug',
         'pastor-alemão',
         'labrador']

print(raças[0])
print(raças[1])
print('labrador' in raças)
"""



def raças_atendimento():
    valor_total= 0
    raças = ['pug', 'pastor-alemão', 'labrador']
    raça = input('Insira uma raça: ')
    if (raça in raças):
        if (raça == 'pug'):
            valor_total = valor_total + 70.99
            print(valor_total)
        elif (raça == 'pastor-alemão'):
            valor_total = valor_total + 120.99
            print(valor_total)
        elif (raça == "labrador"):
            valor_total = valor_total + 110.99
            print(valor_total)
            print("Atendimento disponivel")
    else:
        print("Atendimento indisponivel")

raças_atendimento()
    