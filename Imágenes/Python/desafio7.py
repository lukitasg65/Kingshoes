import turtle
turtle.fillcolor("red")
turtle.begin_fill()
turtle.left(20)
for i in range(4):
    turtle.forward(50)
    turtle.left(90)
turtle.end_fill()
turtle.fillcolor("green")
turtle.begin_fill()
turtle.left(30)
for i in range(4):
    turtle.forward(50)
    turtle.left(90)
turtle.end_fill()
turtle.done()
