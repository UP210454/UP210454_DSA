def prioridad(C):
    if C in ["+", "-"]:
        return 1
    elif C in ["*", "/"]:
        return 2
    elif C in ["^"]:
        return 3
    elif C in ["(", ")"]:
        return 0

infix = "A + ( B * C - ( D / E ^ F ) * G ) * H"
p = infix.split()
p.append(")")
p.insert(0, "(")
stack = []
operadores = ["-", "+", "*", "/", "^"]
posfix = []
contador = 0


for i in range(len(p)):
    if p[i] == "(":
        stack.append(p[i])
    elif p[i] in operadores:
        contador = len(stack)-1
        if (prioridad(p[i])) >= (prioridad(stack[contador])):
            stack.append(p[i])
        else:
            posfix.append(stack.pop())
            stack.append(p[i])
    elif p[i] == ")":
        contador = len(stack)-1
        while stack[contador] != "(":
            posfix.append(stack.pop())
            contador -= 1
        stack.pop()
    else:
        posfix.append(p[i])

print(f"Infix: {infix}")
print(f"Posfix: {posfix}")