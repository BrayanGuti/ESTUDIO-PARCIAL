class Nodo: #CONSTRUCTOR DE LA LISTA
    def __init__(self, data):
        self.data = data
        self.next = None
        
    def __repr__(self):
        return str({self.data})
class lista_simple:
    def __init__(self) -> None:
        self.PTR = None
        self.last = None
    def addNode(self, data):
        p = Nodo(data = data)
        if (self.PTR== None):
            self.PTR=p
            self.last=p
        else:
            self.last.next=p
            self.last=p #en caso de que sea simple
            
    def recorrer(self):
        p = self.PTR
        while(p.next != None):
            print(p, end="->")
            p = p.next
        
        print(p)
        print("")
    
    def repetidos(self, dato):
        cont = 0
        p = self.PTR
        while(p.next != None):
            if(p.data == dato):
                cont += 1
            p = p.next
        return cont
    
    def comparar(self, lista):
        p = self.PTR
        while(p.next != None):
            if(self.repetidos(p.data) != lista.repetidos(p.data)):
                return False
            p = p.next
        return True