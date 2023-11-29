import turtle

def petal(colors):
    for _ in range(8):
        turtle.begin_fill()
        turtle.color(colors)
        turtle.circle(30)
        turtle.right(45)
        turtle.forward(30)
        turtle.end_fill()

def flower(colors):
    turtle.right(110)
    turtle.forward(90)
    turtle.left(90)
    turtle.begin_fill()
    turtle.color(colors)
    turtle.circle(50)
    turtle.end_fill()

def stalk(colors="green"):
    turtle.right(140)
    turtle.penup()
    turtle.forward(40)
    for _ in range(20):
        turtle.begin_fill()
        turtle.color("green")
        turtle.circle(10)
        turtle.left(3)
        turtle.forward(5)
        turtle.end_fill()

petal("blue")
flower("yellow")
stalk()
turtle.right(180)
turtle.penup()
turtle.forward(350)
petal("red")
flower("orange")
stalk()
