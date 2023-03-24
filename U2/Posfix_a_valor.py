def valor(expresion):
    vector = expresion
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
    print(resultado)

valor([5, 5, 5, "+", "+"])
