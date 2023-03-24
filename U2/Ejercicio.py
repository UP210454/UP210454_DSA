def random(inicial, a, b, n):
    numeros = []
    for i in range(n):
        while True:
            inicial = hash(str(inicial))
            num_aleatorio = a + (inicial % (b - a))
            if num_aleatorio not in numeros:
                numeros.append(num_aleatorio)
                break
    return numeros


def burbuja(x):
    lista = x
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(lista) - 1):
            if lista[i] > lista[i + 1]:
                swapped = True
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
    return lista


def binario(lista, valor):
    contador = 0
    li = 0
    ls = len(lista) - 1
    while li <= ls:
        contador += 1
        m = (li + ls) // 2
        if lista[m] == valor:
            return f"El numero {valor} se encuentra en la posicion {m} y se encontró en {contador} pasos."
        elif lista[m] > valor:
            ls = m - 1
        elif lista[m] < valor:
            li = m + 1
    return f"El numero {valor} no se encuentra en la lista."


def imprimirVector(lista):
    for i in range(len(lista)):
        print(lista[i], end=", ")
        if ((i+1) % 10 == 0):
            print()

    print()

lista_desordenada = random("Aarongay", 101, 500, 100)
lista_ordenada = burbuja(lista_desordenada)
print("Lista ordenada")
imprimirVector(lista_ordenada)
num = int(input("Que numero quieres buscar: "))
resultado = binario(lista_ordenada, num)
print(resultado)
