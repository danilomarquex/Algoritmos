def x(num):
	if num % 2 == 0:
		print("O número {} é par!" .format(num))
	else:
		print("O número {} é ímpar!" .format(num))


#PROGRAMA PRINCIPAL!

num = int(input("Digite um número: "))
x(num)