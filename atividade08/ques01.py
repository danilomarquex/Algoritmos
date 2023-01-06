L = []
for i in range(0,21):
    x = int(input("digite o número: "))
    L.append(x)
print(L)
y = int(input("Escolha um número da lista: "))
if y in L:
    print("O número {} se repetiu {} vezes " .format(y, L.count(y)))
else:
    print("O número {} não está na lista {}" .format(y, L))
