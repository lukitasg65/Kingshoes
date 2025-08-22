# -*- coding: utf-8 -*-
def contar_vocales(palabra):
    vocal = 0
    for letra in palabra:
        if letra in "aeiouAEIOUáéíóúÁÉÍÓÚ":
            vocal += 1
    return vocal
frutas = ["Manzanas", "Uvas", "Fresas", "Piñas"]
for fruta in frutas:
    print("Las frutas son:", fruta)
    print("La cantidad de vocales son:", contar_vocales(fruta))
