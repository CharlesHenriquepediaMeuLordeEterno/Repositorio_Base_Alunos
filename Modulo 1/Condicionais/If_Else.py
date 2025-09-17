'''
Saldo = int( input("digite o saldo bancário: ") )
Saque = int( input("digite o valor de saque: ") )

if Saldo >= Saque:
    Saldo -= Saque
    print("Você realizou um saque com sucesso.",Saldo)
else:
    print("Você não possui saldo suficiente para realizar essa operação",Saldo)

nome = (input("Digite o nome do aluno: ") )
nota1 = float( input("Digite a primeira nota: ") )
nota2 = float( input("Digite a segunda nota: ") )
media = (nota1+nota2)/2
if media >= 6 and media <= 7:
    print("O aluno",nome, "Foi aprovado com a nota", media)
elif media >= 8:
    print("O aluno",nome,"Foi aprovado com Louvor com a nota", media)
else:
    print("O aluno", nome, "Foi reprovado com a nota", media)
'''

valor_parte = float(input("Insira o valor parte: "))
porcentagem = float(input("Insira o valor da porcentagem: "))
if porcentagem <=0.0:
    print("Insira um número maior que zero.")
else:
    print()
    valor_total = valor_parte * (porcentagem/100)
    print(valor_total)