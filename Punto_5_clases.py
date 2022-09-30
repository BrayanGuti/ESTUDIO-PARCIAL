class Nodo:
    def __init__(self, dato) -> None:
        self.dato = dato
        self.next = None

class Lista:
    def __init__(self) -> None:
        self.PTR = None
        self.last = None


    def __repr__(self) -> str:
        cadena = ""
        actual = self.PTR
        
        while(actual.next != self.PTR):
            cadena += "[" + str(actual.dato) + "]" + "->"  
            actual = actual.next
        cadena += "[" + str(actual.dato) + "]"  
        actual = actual.next
        
        return(cadena)
    
    def agregar (self, dato)-> None:
        temp = Nodo(dato= dato)
        if(self.PTR == None):
            self.PTR = temp
            self.last = temp
            
        else:
            self.last.next = temp
            self.last = temp
           
        self.last.next = self.PTR

    def agregar_nodos(self, lista2, subespacio) -> None:
        iterador = 1
        actual = self.PTR
        while (iterador < subespacio):
            actual = actual.next
            iterador += 1
        temp = actual.next    
        actual.next = lista2.PTR
        lista2.last = temp.next