class Node:
    def __init__(self, data):
        self.data = data
        self.next =None

    def getData(self):
        return self.data

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def getSize(self):
        return self.size

    def isEmpty(self):
        return True if self.size == 0 else False

    def push(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
        self.size += 1

    def pop(self):
        if not self.isEmpty():
            dato = self.head.getData()
            self.size-=1
            self.head = self.head.next
            return dato
        else:
            print("No se puede hacer pop")
        
    def mostrarDatos(self):
        next = self.head
        for i in range(self.getSize()):
            print(next.getData())
            next = next.next

    def peak(self):
        return self.head.data
    
    def show(self):
        direccion = self.head
        datas = ""
        for i in range(self.size):
            datas += str(direccion.getData()) + " " 
            direccion = direccion.next
        return datas

    def exist(self, exist):
        direccion = self.head
        for i in range(self.size):
            if direccion.getData() == exist:
                return True
            direccion = direccion.next
        return False


pila = Stack()
pila.push("Jose")
pila.push("Maria")
pila.push("Jesus")

print("Pila completa")
pila.mostrarDatos()

pila.pop()
print("Lista después del pop")
pila.mostrarDatos()

print("Show")
print(pila.show())

print("Exist")
print(pila.exist("Fer"))