# -*- coding: utf-8 -*-
lado1 = int(input("Ingrese el valor del lado 1: "))
lado2 = int(input("Ingrese el valor del lado 2: "))
lado3 = int(input("Ingrese el valor del lado 3: "))
if lado1 == lado2 and lado2 == lado3:
    print("Triángulo equilátero")
elif lado1 == lado2 or lado2 == lado3 or lado3 == lado1:
    print("Triángulo isósceles")
else:
    print("Triángulo escaleno")
