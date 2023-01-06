soma_idade = 0
for i in range(0,3):
    idade = int(input("Digite a idade: "))
    soma_idade = soma_idade + idade
media = soma_idade/3
if media > 40:
    print("Acima de 40 anos")
if 25 < media <= 40:
    print("Entre 25 e 40 anos")
if media <= 25:
    print("Menor ou igual a 25 anos")
