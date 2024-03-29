import math
from tkinter import *
from collections import deque

ventana = Tk()
ventana.title("Calculadora")
ventana.configure(background="light sky blue")

i = 0

# Entrada
e_texto = Entry(ventana, font=("Calibri 30"), background="cyan3")
e_texto.grid(row=0, column=0, columnspan=8, padx=5, pady=5)


def enlistar(op):
    op = list(op)
    op.append('a')
    op2 = []
    stack = deque()
    for i in op:

        if i not in ['+', '-', '/', '*', '(', ')', 'a', '^']:
            stack.append(i)
        elif i in ['+', '-', '/', '*', '(', ')', 'a', '^']:
            contador = len(stack) - 1
            a = ''
            while contador >= 0 and stack[contador] not in ['+', '-', '/', '*']:
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
    global funciones
    posfix = []
    contador = 0

    for i in range(len(p)):
        if p[i] == "(":
            stack.append(p[i])
        elif p[i] in operadores or p[i] in funciones:
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
                stack.append(C)
            except:
                return "Math Error"

    resultado = str(stack.pop())
    return resultado


def prioridad(C):
    if C in ["+", "-"]:
        return 1
    elif C in ["*", "/"]:
        return 2
    elif C in funciones:
        return 3
    elif C in ["^"]:
        return 4
    elif C in ["(", ")"]:
        return 0


def click_boton(valor):
    global i
    e_texto.insert(i, valor)
    i += 1

def click_boton_funcion(valor):
    global i
    e_texto.insert(i,valor)
    i = i + 4
def borrar():
    e_texto.delete(0, END)
    i = 0


def operacion():
    ecuacion = e_texto.get()
    a = enlistar(ecuacion)
    b = posfix(a)
    c = valor(b)
    e_texto.delete(0, END)
    e_texto.insert(0, c)
    i = 0


funciones = ["sin", "cos", "tan", "asin", "acos", "atan", "log", "ln", "alog", "aln"]
operadores = ["+", "-", "*", "/", "^"]

# Botones
boton1 = Button(ventana, text="1", width=8, height=4, command=lambda: click_boton(1), background="RoyalBlue1")
boton2 = Button(ventana, text="2", width=8, height=4, command=lambda: click_boton(2), background="RoyalBlue1")
boton3 = Button(ventana, text="3", width=8, height=4, command=lambda: click_boton(3), background="RoyalBlue1")
boton4 = Button(ventana, text="4", width=8, height=4, command=lambda: click_boton(4), background="RoyalBlue1")
boton5 = Button(ventana, text="5", width=8, height=4, command=lambda: click_boton(5), background="RoyalBlue1")
boton6 = Button(ventana, text="6", width=8, height=4, command=lambda: click_boton(6), background="RoyalBlue1")
boton7 = Button(ventana, text="7", width=8, height=4, command=lambda: click_boton(7), background="RoyalBlue1")
boton8 = Button(ventana, text="8", width=8, height=4, command=lambda: click_boton(8), background="RoyalBlue1")
boton9 = Button(ventana, text="9", width=8, height=4, command=lambda: click_boton(9), background="RoyalBlue1")
boton0 = Button(ventana, text="0", width=8, height=4, command=lambda: click_boton(0), background="RoyalBlue1")

boton_borrar = Button(ventana, text="AC", width=8, height=4, command=lambda: borrar(), background="red")
boton_parentesis1 = Button(ventana, text="(", width=8, height=4, command=lambda: click_boton("("),
                           background="RoyalBlue1")
boton_parentesis2 = Button(ventana, text=")", width=8, height=4, command=lambda: click_boton(")"),
                           background="RoyalBlue1")
boton_punto = Button(ventana, text=".", width=8, height=4, command=lambda: click_boton("."), background="RoyalBlue1")

boton_division = Button(ventana, text="/", width=8, height=4, command=lambda: click_boton("/"), background="RoyalBlue1")
boton_multiplicacion = Button(ventana, text="  *", width=8, height=4, command=lambda: click_boton("*"),
                              background="RoyalBlue1")
boton_suma = Button(ventana, text="+", width=8, height=4, command=lambda: click_boton("+"), background="RoyalBlue1")
boton_resta = Button(ventana, text="-", width=8, height=4, command=lambda: click_boton("-"), background="RoyalBlue1")
boton_igual = Button(ventana, text="=", width=8, height=4, command=lambda: operacion(), background="RoyalBlue1")
boton_potencia = Button(ventana, text="^", width=8, height=4, command=lambda: click_boton("^"), background="RoyalBlue1")
boton_seno = Button(ventana, text="sen", width=8, height=4, command=lambda: click_boton_funcion("sin("), background="RoyalBlue1")

# Agregar botones
boton_borrar.grid(row=1, column=0, padx=5, pady=5)
boton_parentesis1.grid(row=1, column=1, padx=5, pady=5)
boton_parentesis2.grid(row=1, column=2, padx=5, pady=5)
boton_division.grid(row=1, column=3, padx=5, pady=5)
boton_seno.grid(row=1, column=4, padx=5, pady=5)

boton7.grid(row=2, column=0, padx=5, pady=5)
boton8.grid(row=2, column=1, padx=5, pady=5)
boton9.grid(row=2, column=2, padx=5, pady=5)
boton_multiplicacion.grid(row=2, column=3, padx=5, pady=5)

boton4.grid(row=3, column=0, padx=5, pady=5)
boton5.grid(row=3, column=1, padx=5, pady=5)
boton6.grid(row=3, column=2, padx=5, pady=5)
boton_suma.grid(row=3, column=3, padx=5, pady=5)

boton1.grid(row=4, column=0, padx=5, pady=5)
boton2.grid(row=4, column=1, padx=5, pady=5)
boton3.grid(row=4, column=2, padx=5, pady=5)
boton_resta.grid(row=4, column=3, padx=5, pady=5)
# boton_tangente.grid(row=4, column=4, padx=5,pady=5)

boton0.grid(row=5, column=1, padx=5, pady=5)
boton_punto.grid(row=5, column=0, padx=5, pady=5)
boton_igual.grid(row=5, column=2, padx=5, pady=5)
boton_potencia.grid(row=5, column=3, padx=5, pady=5)

# boton_logaritmo.grid(row=5, column=4, padx=5, pady=5)

ventana.mainloop()