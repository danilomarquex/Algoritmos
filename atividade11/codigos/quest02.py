dicionario = {}
while True:
    name = input("Digite seu nome: ")
    year = int(input("Digite sua idade: "))
    telefone = int(input("Digite seu telefone: "))
    dicionario[name] = (year,telefone)
    continuar = input("Continuar S ou N: ").upper()
    if continuar == 'S':
           print("-"*40)
    if continuar == 'N':   
           print(dicionario)
           break
selname = input("Escolha um nome desejado para ser removido do nosso banco de dados: ")
certeza = input("Tem certeza disso? S - N ").upper()
if  certeza=='S':
  del[dicionario[selname]]
  print(dicionario)
else:
    print()
print(dicionario)
