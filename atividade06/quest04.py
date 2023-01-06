NOTA = []
N = 0
for i in range(1,11):
    n = float(input("Digite a nota: "))
    N+=n
    NOTA.append(n)
print("Notas: {}" .format(NOTA))
print("Média= {}" .format(N/10))
