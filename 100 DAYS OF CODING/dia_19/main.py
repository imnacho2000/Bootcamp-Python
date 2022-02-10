from turtle import Turtle, Screen

melman = Turtle() 
screen = Screen()


def mover_acostado():
    return melman.setheading(0)
def mover_arriba():
    melman.setheading(90)

def mover_adelante():
    melman.forward(10)

def mover_atras():
    melman.backward(10)

def posicion_inicial():
    melman.clear()
    melman.penup()
    melman.home()
    melman.pendown()

def mover_sentido_contrario():
    pos = melman.heading()
    melman.setheading(pos + 30)

def mover_sentido_reloj():
    pos = melman.heading()
    melman.setheading(pos - 30)


screen.listen()
screen.onkey(key="d", fun=mover_sentido_reloj)
screen.onkey(key="a", fun=mover_sentido_contrario)
screen.onkey(key="w", fun=mover_adelante)
screen.onkey(key="s", fun=mover_atras)
screen.onkey(key="c", fun=posicion_inicial)

screen.exitonclick()