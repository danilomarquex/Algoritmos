dicionario = {}
while True :
    cpf = int(input("Informe seu cpf: "))
    n = input("Informe seu nome: ")
    dicionario[cpf] = n
    continuar = int(input("Continuar :SIM(1) --- NÃO(2) "))
    if continuar == 1:
        print("="*30)
    if continuar == 2:
        print(dicionario)
        break
