#Hacer un algoritmo que dadas dos listas enlazadas circulares PTR1 y PTR2, 
# las cuales representan dos polinomios (Puede asumir que ya están ordenados de manera ascendente o descendente), sume los polinomios dejando la respuesta en PTR1. 
# (Recordar que el coeficiente de un término puede ser negativo) 
# Puede asumir que no existen exponentes negativos.

from clases2 import * # * significa que importa todas las clases
lista1 = linkedList()
lista2 = linkedList()
terminos = int(input("cantidad de términos: "))

for i in range (terminos): 
    coef = int(input("ingrese coeficiente lista 1: "))
    expo = str(input("ingrese exponente lista 1: "))

    lista1.addNode(coef, expo)
    

    coef = int(input("ingrese coeficiente lista 2: "))
    expo = str(input("ingrese exponente lista 2: "))
    lista2.addNode(coef, expo)
    
lista1.recorrer()
lista2.recorrer()
lista1.sumar(lista2)
lista1.recorrer()