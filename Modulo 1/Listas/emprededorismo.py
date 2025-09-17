estoque={   "brigadeiro": [ 600, 1.50],
            "beijinho": [ 600, 1.50],
			"quindim": [ 201, 1.20],
			"paçoca": [ 400, 1.50],
            "bolo": [50, 5.50],
            "sonho": [30, 6.00],
            "cupcake": [20, 7.10],
            "coxinha": [200, 3.00],
            "grostoli": [60, 4.00],
            "sorvete": [50, 20.99],
            "wafer": [200, 3.99],
            "salgadinho": [150, 8.99],
            "bolacha": [55, 2.89],
            "pão": [165, 0.75],
            "pão de queijo": [267, 1.20],
            "croissant": [36, 5.99],
            "esfirra": [51, 6.75],
            "enroladinho": [28, 4.65],
            "churros": [12, 4.00],
            "pamonha": [8, 12.50] }
produto = input("Digite o produto desejado: ")
quantidade = int(input("Digite a quantidade: "))
venda = [ [produto, quantidade] ]
total = 0
if produto in estoque:
  print("Vendas:\n")
  for operação in venda:
    produto , quantidade = operação 
    preço = estoque[produto][1] 
    custo = preço * quantidade
    print("%12s: %3d x %6.2f = %6.2f" %
	  (produto, quantidade,preço,custo))
    estoque[produto][0] -= quantidade 
    total+=custo
else:
   print("Não temos esse produto em nosso estoque")
print(" Custo total: %21.2f\n" % total)
print("Estoque:\n")
for chave, dados in estoque.items(): 
    print("Descrição: ", chave)
    print("Quantidade: ", dados[0])
    print("Preço: %6.2f\n" % dados[1])