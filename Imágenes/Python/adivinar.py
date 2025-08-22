# -*- coding: utf-8 -*-
import random
def contarvocal(palabra):
    vocal = 0
    for i in palabra:
        if i in "aeiouAEIOUáéíóú":
            vocal = vocal + 1
        return vocal
lista = ("Computación","Programación","Informática","Robótica","Tecnología")
palabra = random.choice(lista)
letras = len(palabra)
letrai = palabra[0]
letraf = palabra[letras-1]
print ("Bienvenido, debes adivinar la palabra.")
print ("La palabra tiene", letras, "letras.")
print ("Tiene", contarvocal(palabra),"vocales." )
print ("Inicia con la letra:", letrai)
print ("Termina con la letra:", letraf)
adivina = input("Ingresa la palabra: ")
if adivina == palabra:
    print("¡Bien hecho, adivinaste!")
else:
    print ("¡Intenta nuevamente!")
