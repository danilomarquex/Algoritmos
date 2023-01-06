c=0
l=0
matriz=[]
for i in range(3):    
    matriz.append([])        
    for j in range(3):
        matriz[i].append([l,j,c])
        c=c+1
    l=l+1
    
for i in range(3):
    print("\n")
    for j in range(3):
        print(matriz[i][j],end=" ")
