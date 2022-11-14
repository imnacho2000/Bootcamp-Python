from turtle import Turtle, Screen
import random
from dia18 import rgb_colors

"""Formando a la tortuga"""
melman = Turtle()
melman.shape("turtle")
melman.color("purple")


# pos = -90
# for n in range(4):
#     melman.seth(pos)
#     melman.forward(100)
#     pos -= 90


# for n in range(50):
#     melman.pendown()
#     melman.forward(10)
#     melman.penup()
#     melman.forward(10)

# def recorriendo(num):
#     pos = 360 / num
#     for n in range(num):
#         melman.forward(100)
#         melman.right(pos)

# for n in range(3,11):
#     recorriendo(n)

screen = Screen().colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tupla_colores = (r,g,b)
    return tupla_colores


# grosor = 0.1
# for n in range(100):
#     cantidad_pasos = random.randint(50,100)
#     posicion = random.randrange(0, 360, 90)
#     list = ["black","green","red","blue","purple","grey","brown"]
#     coloR = random.choice(list)
#     melman.pensize(grosor)
#     melman.color(random_color())
#     melman.forward(cantidad_pasos)
#     melman.seth(posicion)
#     grosor += 0.1
    



for n in range(100):
    melman.speed(0)
    melman.circle(100)
    melman.setheading(melman.heading() + 10)

    










"""Para no cerrar la pantalla"""
screen = Screen() 
screen.exitonclick()