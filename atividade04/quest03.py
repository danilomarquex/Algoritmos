while True:
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    if idade >= 40:
        x = idade
        print("{} tem {} anos" .format(nome, idade))
    if idade < 40:
        y = idade
        print("Nenhum com idade igual ou maior a 40anos")
    cont = int(input("Deseja continuar? (1-SIM  2-NÃO)"))
    if cont == 2:
        break