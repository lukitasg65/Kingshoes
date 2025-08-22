# -*- coding: utf-8 -*-
import turtle
hexa = turtle.Turtle()
hexa.color("Blue")
hexa.pensize(5)
hexa.fillcolor("Green")
hexa.begin_fill()
for i in range(6):
    hexa.forward(100)
    hexa.right(60)
hexa.end_fill()
turtle.done()
