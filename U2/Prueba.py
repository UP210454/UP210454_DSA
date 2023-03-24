import math
from collections import deque

def enlistar(op):
    op = list(op)
    op.append('b')
    op2 = []
    stack = deque()
    for i in op:
        if i not in ['+', '-', '/', '*', '(', ')', 'b', '^', "(-)"]:
            stack.append(i)
        elif i in ['+', '-', '/', '*', '(', ')', 'b', '^']:
            contador = len(stack) - 1
            b = ''
            while contador >= 0 and stack[contador] not in ['+', '-', '/', '*']:
                b = b + stack.popleft()
                contador -= 1
            if b != '':
                op2.append(b)
            if i != 'b':
                op2.append(i)
    return op2


def posfix(expresion):
    p = expresion
    p.append(")")
    p.insert(0, "(")
    stack = []
    operadores = ["-", "+", "*", "/", "^"]
    global funciones
    posfix = []
    contador = 0

    for i in range(len(p)):
        if p[i] == "(":
            stack.append(p[i])
        elif p[i] in operadores or p[i] in funciones:
            contador = len(stack) - 1
            if (prioridad(p[i])) > (prioridad(stack[contador])):
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
            posfix.append(p[i])
    return posfix


def valor(expresion):
    vector = expresion
    vector.append(")")
    i = 0
    resultado = 0
    stack = []
    global operadores
    while vector[i] != ")":
        if vector[i] in operadores:
            B = float(stack.pop())
            A = float(stack.pop())
            if vector[i] == "*":
                C = A * B
            elif vector[i] == "/":
                C = A / B
            elif vector[i] == "-":
                C = A - B
            elif vector[i] == "+":
                C = A + B
            elif vector[i] == "^":
                C = A ** B
            stack.append(C)
        elif vector[i] in funciones:
            A = float(stack.pop())
            try:
                if vector[i] == "sin":
                    C = math.sin(math.radians(A))
                elif vector[i] == "cos":
                    C = math.cos(math.radians(A))
                elif vector[i] == "tan":
                    C = math.tan(math.radians(A))
                elif vector[i] == "asin":
                    C = math.degrees(math.asin(A))
                elif vector[i] == "acos":
                    C = math.degrees(math.acos(A))
                elif vector[i] == "atan":
                    C = math.degrees(math.atan(A))
                elif vector[i] == "log":
                    C = math.log10(A)
                elif vector[i] == "ln":
                    C = math.log(A, math.e)
                elif vector[i] == "alog":
                    C = 10 ** A
                elif vector[i] == "aln":
                    C = math.e ** A
                C = round(C)
                stack.append(C)
            except:
                return "Math Error"
        else:
            stack.append(vector[i])
        i += 1
    resultado = stack.pop()
    return resultado


def prioridad(C):
    if C in ["+", "-"]:
        return 1
    elif C in ["*", "/"]:
        return 2
    elif C in funciones:
        return 4
    elif C in ["^"]:
        return 3
    elif C in ["(", ")"]:
        return 0


funciones = ["sin", "cos", "tan", "asin", "acos", "atan", "log", "ln", "alog", "aln"]
operadores = ["+", "-", "*", "/", "^"]

#n = "(8+(8^2-4*1*15)^(1/2))/(2*1)"
#n = "2+asin(1.7071-1)+3"
#n = "sin(45)^2+cos(45)^2"
#n = "1/(100+1/(100+1/(100+1/100)))"
#n = "2*log(94+2*3)^3"
#n = "3+(9*2-3/6)^(1/2)*5"
n = "atan(0.5)"

print(f"Expresión normal: {n}")
a = enlistar(n)
print(f'Expresión con espacios: {a}')
b = posfix(a)
print(f'Expresion en posfix: {b}')
c = valor(b)
print(f'Resultado: {c}')
