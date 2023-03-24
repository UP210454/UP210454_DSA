from collections import deque
def enlistar(op):
    op = list(op)
    op.append('a')
    op2 = []
    stack = deque()
    for i in op:

        if i not in ['+','-','/','*','(',')','a','^']:
            stack.append(i)
        elif i in ['+','-','/','*','(',')','a','^']:
            contador = len(stack)-1
            a = ''
            while contador >= 0 and stack[contador] not in ['+','-','/','*']:
                a = a + stack.popleft()
                contador -= 1
            if a != '':
                op2.append(a)
            if i != 'a':
             op2.append(i)
    return op2

def posfix(expresion):
    p = expresion
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
            contador = len(stack) - 1
            if (prioridad(p[i])) >= (prioridad(stack[contador])):
                stack.append(p[i])
            else:
                posfix.append(stack.pop())
                stack.append(p[i])
        elif p[i] == ")":
            contador = len(stack) - 1
            while stack[contador] != "(":
                posfix.append(stack.pop())
                contador -= 1
            stack.pop()
        else:
            posfix.append(int(p[i]))
    return posfix

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
            B = float(stack.pop())
            A = float(stack.pop())
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
    return resultado

def prioridad(C):
    if C in ["+", "-"]:
        return 1
    elif C in ["*", "/"]:
        return 2
    elif C in ["^"]:
        return 3
    elif C in ["(", ")"]:
        return 0

n = str(input("Introduce la ecuacion"))
a = enlistar(n)
print(a)
b = posfix(a)
print(b)
c = valor(b)
print(c)