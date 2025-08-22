# -*- coding: utf-8 -*-
import turtle
lados = int(input("Ingrese el número de lados: "))
borde = int(input("Ingrese el grosor del borde (1 - 5): "))
relleno = input("Ingrese el color de relleno: ")
cborde = input("Ingrese el color de borde: ")
angu = 360/lados
poli = turtle.Turtle()
poli.penup()
poli.goto(-50,-50)
poli.pendown()
poli.pensize(borde)
poli.speed(1)
poli.color(cborde)
poli.fillcolor(relleno)
poli.begin_fill()
for i in range(lados):
    poli.forward(100)
    poli.left(angu)
poli.end_fill()
turtle.done()
