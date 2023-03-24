lista1 = [-5, 2, 3, 6, 1, 9, 14]
lista2 = [-3, 0, 5, 7, 9, 10, 14]

def desordenado(list, value):
    for i in range(len(list)):
        if list[i] == value:
            return i
    return None


def ordenado(list, value):
    for i in range(len(list)):
        if list[i] == value:
            return i
        elif list[i] > value:
            break
    return None

num = int(input("Introduce el numero que quieres buscar en la lista ordenada: "))
posicion = ordenado(lista2, num)
print(f"El numero {num} se encuentra en la posicion {posicion}")

num2 = int(input("Introduce el numero que quieres buscar en la lista desordenada: "))
posicion2 = desordenado(lista1, num2)
print(f"El numero {num2} se encuentra en la posicion {posicion2}")