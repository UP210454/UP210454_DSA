palabra = input("Introduce la palabra: ")
palabra2 = palabra[::-1]

if palabra == palabra2:
    print("Es polindromo")
else:
    print("No es polindromo")

palabra3 = str(input("Introduce la frase: "))
palabra3 = palabra3.replace(" ", "")
palabra4 = palabra3[::-1]

if palabra3 == palabra4:
    print("Es polindromo")
else:
    print("No es polindromo")