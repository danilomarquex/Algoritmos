matriz= [ [ 0,0 ], [ 0,0 ] ]
for l in range (0,2):
    for c in range (0,2):
        matriz [l] [c]= int(input(f"Digite um número [{l} , {c}]:"))
print("="*30)
for l in range (0,2):
    for c in  range (0,2):
        print(f"[{matriz [l] [c]:^5}]", end = ' ' )
    print()
print("="*30)
matriz [0] [0]= matriz[0][0] / matriz[0][0]
matriz [0][1]= matriz[0][1] /matriz [0][0]
matriz [1][0]= matriz [1][0] / matriz [1] [1]
matriz [1][1]= matriz [1][1] / matriz [1][1]
for l in range (0,2):
    for c in range (0,2):
        print(f"[{matriz [l] [c]: ^5}]", end = ' ')
    print()