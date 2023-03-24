class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

class Queue:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def getSize(self):
        return self.size
    
    def isEmpty(self):
        return True if not self.head else False
    
    def enqueue(self, data):
        newNode = Node(data)
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.size += 1

    def dequeue(self):
        dato = None
        if not self.isEmpty():
            old = self.head
            dato = self.head.getData()
            self.size -= 1
            self.head = self.head.next
            del old
            if self.isEmpty():
                self.tail = None
        return dato
        
    def show(self):
        direccion = self.head
        datas = "head --> "
        for i in range(self.size):
            datas += str(direccion.getData()) + " --> "
            direccion = direccion.next
        datas += " tail"
        return datas

    def getFirst(self):
        if not self.isEmpty():
            return self.head.data
        else:
            print("Fila vacía")

    def getLast(self):
        if not self.isEmpty():
            return self.tail.data
        else:
            print("Fila vacía")

    def search(self, exist):
        direccion = self.head
        for i in range(self.size):
            if direccion.getData() == exist:
                return True
            direccion = direccion.next
        return False

    
fila = Queue()
fila.enqueue(5)
fila.enqueue(10)
fila.enqueue(15)
fila.enqueue(20)
print(fila.show())
fila.dequeue()
print(fila.show())
fila.dequeue()
print(fila.show())
fila.dequeue()
print(fila.show())
fila.dequeue()
print(fila.show())
fila.dequeue()
fila.getFirst()
fila.getLast()
print("---------------")
fila.enqueue("Hector")
fila.enqueue("Aaron")
fila.enqueue("Eliseo")
fila.enqueue("Jorge")
print(fila.show())
print(f'First: {fila.getFirst()}, Last: {fila.getLast()}')
print(fila.search("Axel"))
print(fila.search("Aaron"))


fila2 = Queue()
fila2.enqueue("Hector")
print(fila2.show())
fila2.dequeue()
print(fila2.show())