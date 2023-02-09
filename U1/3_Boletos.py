sumatoria = 0
pesos = int(input("Cuanto dinero tienes? \n"))
boletos=0
resto = 0
for i in range (1,1000):
    sumatoria = sumatoria + i
    if pesos >= sumatoria:
        boletos = boletos + 1

print(f'Con ${pesos}, puedes comprar {boletos} boletos.')

