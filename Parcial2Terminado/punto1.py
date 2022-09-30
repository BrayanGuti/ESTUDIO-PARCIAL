#Escribir un algoritmo que verifique si dos listas enlazadas simples son semejantes. 
# Dos listas enlazadas son semejantes si tienen los mismos elementos (datos), no importa el orden. 
# Si un elemento se repite en una lista en la otra debe repetirse igual número de veces.
#NOTA: Para este ejercicio no se permite ordenar ninguna lista.

from clases import *
lista1 = lista_simple()
lista2 = lista_simple()
cant = int(input("Ingrese la cantidad de nodos de las listas: "))

for i in range (cant):
    info = int(input("Ingrese la data lista 1: "))
    lista1.addNode(info)
    info2 = int(input("Ingrese la data lista 2: "))
    lista2.addNode(info2)

lista1.recorrer()
lista2.recorrer()
if (lista1.comparar(lista2)):
    print("Son semejantes")
else:
    print("no son semejantes")


