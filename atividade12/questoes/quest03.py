def compara():
	x=int(input("Digite um valor: "))
	y=int(input("Digite outro valor: "))
	if x>y:
		print("{} é o maior valor!" .format(x))
	if y>x:
		print("{} é o maior valor!" .format(y))
	if y==x:
		print("{} e {} são iguais!" .format(x, y))

compara()

