"""
5. Dadas dos listas circulares ya creadas PTR1 y PTR2, hacer un algoritmo que inserte
los elementos de PTR2 a PTR1. Posibles formas:
a. De manera ordenada (Puede asumir no repetidos)
b. Indicando una posición inicial en PTR1 donde después ó antes de esta
vamos a insertar todos los elementos de PTR2.

"""




class Nodo:
    def __init__(self, info) -> None:
        self.info = info
        self.next = None
        
    def __repr__(self) -> str:
        return str(self.info)
class lista:
    def __init__(self) -> None:
        self.PTR = None
        self.last = None
    def addnode(self, info):
        nodo = Nodo(info)
        if (self.PTR == None):
            self.PTR = nodo
            self.last = nodo
        else:
            self.last.next = nodo
            self.last = nodo
        self.last.next = self.PTR
    def __repr__(self) -> str:
        selecter = self.PTR
        cadena = ""
        while(selecter != self.last):
            cadena += (f"{selecter} --> ")
            selecter = selecter.next
        cadena += (f"{selecter}")
        return (cadena)
    def addWithAnotherList(self, list2):
        selecter = self.PTR
    
