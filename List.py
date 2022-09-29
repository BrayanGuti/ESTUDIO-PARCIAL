class Nodo:
    
    def __init__(self, dato) -> None:
        self.dato = dato
        self.next = None
        self.anterior = None
    
    def ver_dato(self):
        return self.dato
    
    def traer_siguiente(self):
        return self.next
    
    def corregir (self, nuevo_dato) -> None:
        self.dato = nuevo_dato
    
    def colocar_siguiente(self, dato_siguiente) -> None:
        self.next = dato_siguiente

class Lista:

    def __init__(self) -> None:
        self.PTR = None    
    
    def agregar (self, dato):
        temp = Nodo(dato= dato)
        temp.colocar_siguiente(self.PTR)
        self.PTR = temp
    
    def ver_lista(self):
        actual = self.PTR
        cadena = ""
        while actual != None:
            cadena += "->" + "[" + str(actual.ver_dato()) + "]"
            actual = actual.traer_siguiente()
        print(cadena)
    
    def buscar(self, dato):
        actual = self.PTR
        while actual != None:
            if (dato  == actual.ver_dato()):
                return True
            else:
                actual = actual.next
        return False
    
    def borrar (self, dato):
        actual = self.PTR
        previo = None
        encontrado = False
        while not encontrado:
            if(actual != None):
                if(actual.ver_dato() == dato):
                    encontrado = True
                else:
                    previo = actual
                    actual = actual.traer_siguiente()
            else:
                break
        if(actual !=  None):
            if(previo == None):
                self.PTR = actual.traer_siguiente()
            else:
                previo.colocar_siguiente(actual.traer_siguiente())
    
    
    def eliminar_diferencia(self, List2):
        actual = self.PTR
        while (actual != None):
            if(List2.buscar(actual.ver_dato()) ==  True):
                self.borrar(actual.ver_dato())
                actual = actual.traer_siguiente()
            else:
                actual = actual.traer_siguiente()
    

    def mostrar_diferrencias(self, List2):
        actual = self.PTR
        contador = 0
        cadena = ""
        while (actual != None):
            if(List2.buscar(actual.ver_dato()) ==  False):
                cadena += "[" + str(actual.ver_dato()) + "]->"    
                contador += 1
                actual = actual.traer_siguiente()
            else:
                actual = actual.traer_siguiente()
        print(F"Hay una cantidad de datos diferentes de {contador} y son: {cadena}")


