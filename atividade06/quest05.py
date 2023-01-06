l = []
for i in range(1,11):
    n = input("Digite seu nome: ")
    tam = len(n)
    if tam > 10:
        print("Só é permitido no máximo 10 caractéres!")
    if tam <=10:
        l.append(n)
con = input("Consulte os nomes contidos na lista: ")
if len(con) > 10:
    print("Só é permitido no máximo 10 caractéres!")
if len(con) <= 10:
    if con in l:
        print(con)
    else:
        print("{} não está contido na lista" .format(con))
