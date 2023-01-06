soma_nota = 0
quant_alunos = 0
while True:
    idade = int(input("Leia a idade: "))
    resp = int(input("Deseja continuar? (1- Sim 2- Não) "))
    soma_nota+=idade 
    quant_alunos+= 1
    if resp == 2:
        break

media = soma_nota/quant_alunos
print("A média é {}" .format(media))

if media > 40:
    print("Acima de 40 anos")
if 25 < media <= 40:
    print("Entre 25 e 40 anos")
if media <= 25:
    print("Menor ou igual a 25 anos")