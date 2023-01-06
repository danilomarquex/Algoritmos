ma = [[0,0] , [0,0]]
for x in range(0,2):
    for c in range(0,2):
        ma [x][c] = int(input(f"Digite um número [{x} ,  {c}]: "))
print("=" * 30)

for x in range(0,2):
    for c in range(0,2):
        print(f"[{ma [x] [c]:^5}]", end = '')
    print()
print("=" * 30)
ma[0] [0] = ma[0][0] / ma[0][0]
ma[0] [1] = ma[0][1] / ma[0][0]
ma[1] [0] = ma[1][0] / ma[1][1]
ma[1] [1] = ma[1][1] / ma[1][1]

for x in range (0,2):
    for c in range(0,2):
        print(f"[{ma[x] [c]:^5}]", end = '')
    print()