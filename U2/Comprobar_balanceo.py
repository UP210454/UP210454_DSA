def comprobar_balanceo(expresion):
    pila = []
    for caracter in expresion:
        if caracter in ["(", "{"]:
            pila.append(caracter)
        elif caracter in [")", "}"]:
            if len(pila) == 0:
                return False
            ultimo_caracter = pila.pop()
            if (caracter == ")" and ultimo_caracter != "(") or (caracter == "}" and ultimo_caracter != "{"):
                return False
    return len(pila) == 0


print(comprobar_balanceo("())("))