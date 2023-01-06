dicionario = {}
while True :
    cpf = int(input("Informe seu cpf: "))
    n = input("Informe seu nome: ")
    dicionario[cpf] = n
    continuar = int(input("Continuar :SIM(1) --- NÃO(2): "))
    if continuar == 1:
        print("="*30)
    if continuar == 2:
        print(dicionario)
        break
selecpf=int(input("Escolha o CPF desejado: "))
if selecpf in dicionario:
    print(dicionario[selecpf])
else:
    print("O cpf indicado não existe em nosso banco de dados!!")
