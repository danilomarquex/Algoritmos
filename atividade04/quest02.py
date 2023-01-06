x=y=" " 
for i in range(1,11):
    n = input("Digite o nome: ")
    i = int(input("Digite a idade: "))
    if i >= 18:
        x = i
        print("{} tem {} anos!" .format(n, i))
    if i < 18:
        y = i
        print("Nenhum maior de 18.")
