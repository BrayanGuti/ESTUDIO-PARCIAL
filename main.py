from practica import * # * significa que importa todas las clases
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