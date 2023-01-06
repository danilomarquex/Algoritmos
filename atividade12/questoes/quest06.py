def compara(x,y):
	if x > y:
		print("{} é o maior valor" .format(x))
	if y > x:
		print("{} é o maior valor" .format(y))
	if y == x:
		print("Os valores são iguais")


#PROGRAMA PRINCIPAL

x = int(input("Digite um valor: "))
y = int(input("Digite outro valor: "))

compara(x,y)
