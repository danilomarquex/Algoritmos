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
selname=input("Escolha um nome armazenado no nosso banco de dados: ")
if selname in dicionario :
  print(f"Nome : {selname} --- Idade / Telefone {dicionario [selname]}")
else:
    print("Nome não encontrado no nosso banco de dados")
