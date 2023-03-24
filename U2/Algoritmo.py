def valor(ecuacion):
    vector = str(ecuacion)
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
    #print(resultado)
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

def infix(ecuacion):
    infix = ecuacion
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

    return posfix

from tkinter import *

ventana=Tk()
ventana.title("Calculadora")

i=0

#Entrada
e_texto = Entry(ventana, font= ("Calibri 20"))
e_texto.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

#Funciones
def click_boton(valor):
    global i
    e_texto.insert(i,valor)
    i+=1

def borrar():
    e_texto.delete(0,END)
    i=0

def operacion():
    ecuacion=e_texto.get()
    infi=infix(ecuacion)
    resultado = valor(infi)
    e_texto.delete(0,END)
    e_texto.insert(0,resultado)
    i=0

#Botones
boton1 = Button(ventana, text="1", width=5, height=2, command=lambda:click_boton(1))
boton2 = Button(ventana, text="2", width=5, height=2, command=lambda:click_boton(2))
boton3 = Button(ventana, text="3", width=5, height=2, command=lambda:click_boton(3))
boton4 = Button(ventana, text="4", width=5, height=2, command=lambda:click_boton(4))
boton5 = Button(ventana, text="5", width=5, height=2, command=lambda:click_boton(5))
boton6 = Button(ventana, text="6", width=5, height=2, command=lambda:click_boton(6))
boton7 = Button(ventana, text="7", width=5, height=2, command=lambda:click_boton(7))
boton8 = Button(ventana, text="8", width=5, height=2, command=lambda:click_boton(8))
boton9 = Button(ventana, text="9", width=5, height=2, command=lambda:click_boton(9))
boton0 = Button(ventana, text="0", width=13, height=2, command=lambda:click_boton(0))

boton_borrar = Button(ventana, text="AC", width=5, height=2, command=lambda:borrar())
boton_parentesis1 = Button(ventana, text="(", width=5, height=2, command=lambda:click_boton("("))
boton_parentesis2 = Button(ventana, text=")", width=5, height=2, command=lambda:click_boton(")"))
boton_punto = Button(ventana, text=".", width=5, height=2, command=lambda:click_boton("."))

boton_division = Button(ventana, text="/", width=5, height=2, command=lambda:click_boton("/"))
boton_multiplicacion = Button(ventana, text="  *", width=5, height=2, command=lambda:click_boton("*"))
boton_suma = Button(ventana, text="+", width=5, height=2, command=lambda:click_boton("+"))
boton_resta = Button(ventana, text="-", width=5, height=2, command=lambda:click_boton("-"))
boton_igual = Button(ventana, text="=", width=5, height=2, command=lambda:operacion())

#Agregar botones
boton_borrar.grid(row= 1,column=0 ,padx=5,pady=5)
boton_parentesis1.grid(row= 1,column= 1,padx=5,pady=5)
boton_parentesis2.grid(row= 1,column= 2,padx=5,pady=5)
boton_division.grid(row= 1,column= 3,padx=5,pady=5)

boton7.grid(row= 2,column= 0,padx=5,pady=5)
boton8.grid(row= 2,column= 1,padx=5,pady=5)
boton9.grid(row= 2,column= 2,padx=5,pady=5)
boton_multiplicacion.grid(row= 2,column= 3,padx=5,pady=5)

boton4.grid(row= 3,column= 0,padx=5,pady=5)
boton5.grid(row= 3,column= 1,padx=5,pady=5)
boton6.grid(row= 3,column= 2,padx=5,pady=5)
boton_suma.grid(row= 3,column= 3,padx=5,pady=5)

boton1.grid(row= 4,column= 0,padx=5,pady=5)
boton2.grid(row= 4,column= 1,padx=5,pady=5)
boton3.grid(row= 4,column= 2,padx=5,pady=5)
boton_resta.grid(row= 4,column= 3,padx=5,pady=5)

boton0.grid(row= 5,column= 0,padx=5,pady=5,columnspan=2)
boton_punto.grid(row= 5,column= 2,padx=5,pady=5)
boton_igual.grid(row=5,column=3, padx=5,pady=5)




ventana.mainloop()