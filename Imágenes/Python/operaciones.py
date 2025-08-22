# -*- coding: utf-8 -*-
print ("**Elige una opción**")
print ("-----------------")
print ("1)Sumar")
print ("2)Restar")
print ("3)Multiplicar")
print ("4)Dividir")
print ("5)Salir")
print ("-----------------")
opci = 0
while opci < 5:
    opci = int(input("Ingrese una opción: "))
    if opci == 1:
        print("Seleccionó la opción sumar")
        v1 =int(input("Ingrese el primer valor: "))
        v2 =int(input("Ingrese el segundo valor: "))
        total = v1 + v2
        print ("El resultado es:", total)
    if opci == 2:
        print("Seleccionó la opción restar")
        v1 =int(input("Ingrese el primer valor: "))
        v2 =int(input("Ingrese el segundo valor: "))
        total = v1 - v2
        print ("El resultado es:", total)
    if opci == 3:
        print("Seleccionó la opción multiplicar")
        v1 =int(input("Ingrese el primer valor: "))
        v2 =int(input("Ingrese el segundo valor: "))
        total = v1 * v2
        print ("El resultado es:", total)
    if opci == 4:
        print("Seleccionó la opción dividir")
        v1 =int(input("Ingrese el primer valor: "))
        v2 =int(input("Ingrese el segundo valor: "))
        total = v1 / v2
        print ("El resultado es:", total)
    if opci == 5:
       break
