def cuadratica(a, b, c):
    return (-b+(b**2 - 4 * a * c)**.5)/(2*a)


y = cuadratica(1, -8, 15)
print(y)
