from Punto_5_clases import Nodo, Lista

List = Lista()
List.agregar("hola")
List.agregar(3)
List.agregar(4)


List2 = Lista()
List2.agregar(1)
List2.agregar(2)
List2.agregar(3)
List2.agregar(5)
List2.agregar(12312312)
List.agregar_nodos(List2, 3)
print(List)