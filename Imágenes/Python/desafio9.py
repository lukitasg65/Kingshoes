# -*- coding: utf-8 -*-
print("**Conversor de unidades**")
while True:
    print("\n---Elige una opción---")
    print("1) Longitud")
    print("2) Temperatura")
    print("3) Tiempo")
    print("4) Salir")
    opc = int(input("Ingresa una opción: "))
    if opc == 1:
        print("\nConvertir de metros a centímetros")
        metros = float(input("Ingresa la cantidad de metros: "))
        print("El resultado en cm es:", metros * 100)
    elif opc == 2:
        print("\nConvertir de grados Celsius a grados Fahrenheit")
        celsius = float(input("Ingresa los grados Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print("Los grados Fahrenheit son:", fahrenheit)
    elif opc == 3:
        print("\nConvertir de minutos a segundos")
        minutos = float(input("Ingresa los minutos: "))
        print("Los segundos son:", minutos * 60)
    elif opc == 4:
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Intenta nuevamente.")
