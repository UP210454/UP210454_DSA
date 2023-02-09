import random
aleatorio = random.randint(1,50)
contador = 1
numero = int(input("Dame un numero: "))
while numero != aleatorio:
    if numero < aleatorio:
        print("Subele")
        contador+=1
    else:
        print("Bajale")
        contador+=1
    numero = int(input("Dame otro numero: "))

print(f'Has ganado con {contador} intentos.')