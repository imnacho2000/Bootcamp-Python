from turtle import Screen
from levels import Level
from autos import Autos
from tortuga import Tortuga
import time

screen = Screen()

screen.setup(width=800,height=600)
screen.bgcolor("white")
screen.tracer(0)
screen.title("Cruzando la tortuga! by Nachota")

personaje = Tortuga()
score = Level()
autitos = Autos()

screen.listen()

screen.onkey(personaje.mover,"Up")
screen.onkey(personaje.abajo,"Down")

game_is_on = True


while game_is_on:
    time.sleep(0.1)
    screen.update()
    autitos.crear()  
    autitos.mover()
    
    if(personaje.posInicial()):
        score.aumentar()
        personaje.ini()
        autitos.aumentarVelocidad()
    
    for auto in autitos.lista_autos:
        if(auto.distance(personaje) < 20):
            score.gameover()
            game_is_on = False


screen.exitonclick()