from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500,height=400)

seleccion = screen.textinput(title="Haz tu apuesta", prompt="Que tortuga crees que ganara?")


lista_tortugas = []

lista_colores = ["purple","red","blue","green","yellow"]


pos = 0
posy = 0
for n in range(5):
    melman = Turtle()
    melman.shape("turtle")
    melman.penup()
    melman.goto(x=-250, y=posy)
    melman.color(lista_colores[pos])
    pos += 1
    posy += 25
    lista_tortugas.append(melman)

race = False
if seleccion:
    race = True 
while race:
    for n in lista_tortugas:
        if n.xcor() < 250:
            pasos = random.randint(0,5)
            n.forward(pasos)
        else:
            ganador = n.pencolor()
            if seleccion == ganador:
                print(f"Ganaste!, la tortuga con color {ganador} gano!")
            else:
                print(f"Perdiste!, la tortuga ganadora fue {ganador}!")
            race = False

screen.exitonclick()