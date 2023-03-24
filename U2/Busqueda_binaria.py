def binario(lista, valor):
    contador = 0
    li = 0
    ls = len(lista) - 1
    while li <= ls:
        contador += 1
        m = (li+ls)//2
        if lista[m] == valor:
            return f"El numero {valor} se encuentra en la posicion {m} y se encontró en {contador} pasos."
        elif lista[m] > valor:
            ls = m - 1
        elif lista[m] < valor:
            li = m + 1
    return f"El numero {valor} no se encuentra en la lista."


lista = [-3, 0, 1, 5, 7, 9]
num = int(input("Introduce el numero que quieres buscar: \n"))
resultado = binario(lista, num)
print(resultado)