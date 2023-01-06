turma = [[] , []]
while True:
    nome=input("Digite o nome: ")
    sexo=input("F-feminino M-Masculino: ").upper()
    nota=float(input("Nota: "))
    if sexo=="F":
        turma[0].append([nome,nota])
    elif sexo=="M":
        turma[1].append([nome,nota])
    else:
        print("Sexo inválido!!..",end=" ")
    resp=input("Deseja continuar (S-sim N-não)?")
    if resp.upper()=="N":
        break
print("nome e nota do(s) menino(s) da turma{}" .format(turma[1]))
