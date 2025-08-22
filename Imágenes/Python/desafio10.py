# -*- coding: utf-8 -*-
usuario = ""
clave = 0
while usuario != "Tbox" or clave != 12345:
    usuario = input("Nombre de usuario: ")
    clave = int(input("Ingresa la clave: "))
    if usuario != "Tbox" or clave != 12345:
        print("Intente nuevamente")
print("Bienvenido al sistema")
