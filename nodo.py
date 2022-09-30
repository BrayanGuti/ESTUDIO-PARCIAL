


class Nodo: 
    def __init__(self,infor) -> None:
        self.infor = infor
        self.next = None
    def __repr__(self):
        return (self.infor)

class Lista: 
    def __init__(self) -> None:
        self.PTR = None
        self.last = None

    def addnode (self,infor):
        nodo = Nodo(infor=infor)
        if (self.PTR == None):
            self.PTR = nodo
            self.last = nodo
        else:
            self.last.next = nodo
            self.last = nodo
    def recorrer (self):
        camino = self.PTR
        while (camino != None):
            print (camino)
            camino = camino.next

    def eliminar (self,lista2):

        camino = self.PTR
        camino2 = lista2.PTR
        
        while (camino.next != None ):
            camino2 = lista2.PTR
            while (camino2 != None ):
                if ( camino.next.infor == camino2.infor and camino.next != self.last):
                        camino.next = camino.next.next
                elif ( camino.next.infor == camino2.infor and camino.next == self.last): 
                    camino.next = None
                    self.last = camino  
                camino2 = camino2.next 
            camino = camino.next
        camino = self.PTR
        camino2= lista2.PTR
        while (camino2 != None):
            if (camino2.infor == camino.infor):
                self.PTR = camino.next
            camino2 = camino2.next

        