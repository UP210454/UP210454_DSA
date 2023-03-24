def desplazar_derecha(lista, n):
    return lista[-n:] + lista[:-n]


def desplazar_izquierda(lista, n):
    return lista[n:] + lista[:n]


lista = [5, 2, 1, 6, 3, 4, 7, 9]
print(lista)
print(desplazar_derecha(lista, 2))
print(desplazar_izquierda(lista, 2))
