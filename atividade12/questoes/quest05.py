def compara(x,y):
	if x == y:
		print("Os valores são iguais.")
	else:
		print("Os valores {} e {} são diferentes." .format(x, y))


#PROGRAMA PRINCIPAL

x = int(input("Digite um valor: "))
y = int(input("Digite outro valor: "))
compara(x, y)
