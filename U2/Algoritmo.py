def prioridad(C):
    if C in ["+", "-"]:
        return 1
    elif C in ["*", "/"]:
        return 2
    elif C in ["^"]:
        return 3
    elif C in ["(", ")"]:
        return 4
    else:
        return 0






vector = [5,6,2,"+","*",12,4,"/","-"]
vector.append(")")
i = 0
resultado = 0
stack = []
while vector[i] != ")":
    if type(vector[i]) == int:
        stack.append(vector[i])
    elif type(vector[i]) == str:
        B = stack.pop()
        A = stack.pop()
        if vector[i] == "+":
            C = A + B
        elif vector[i] == "-":
            C = A - B
        elif vector[i] == "*":
            C = A * B
        elif vector[i] == "/":
            C = A / B
        elif vector[i] == "^":
            C = A ** B
        stack.append(C)
    i += 1

resultado = stack.pop()
print (resultado)

for item in vector:
    if type(item) == str:
        print(f'El operador {item} tiene una prioridad {prioridad(item)}')
    elif type(item) == int:
        print(f'El numero {item} tiene una prioridad {prioridad(item)}')