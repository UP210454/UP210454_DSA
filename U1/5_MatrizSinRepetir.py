from random import randrange
N=int(input("Dame la dimension de la matriz: "))
lista = [[0 for j in range(N)] for i in range(N)]
fila=0
columna=0
while fila<N:
    igual=False
    a=randrange(1,((N**2) +1))
    for fila1 in range(N):
        for columna1 in range(N):
            if (lista[fila1][columna1]==a):
                igual=True
    if igual == False:
        lista[fila][columna]=a
        columna+=1
        if columna==N:
            columna=0
            fila+=1
print(lista)