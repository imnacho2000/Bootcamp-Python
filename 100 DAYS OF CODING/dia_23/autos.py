from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)
pasos = 5
velocidad = 10

class Autos():
    def __init__(self):
        self.pasos = pasos
        self.velocidad = velocidad
        self.lista_autos = []

    def colorRandom(self):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        tupla_colores = (r,g,b)
        return tupla_colores
    
    def mover(self):
        for n in self.lista_autos:
            n.backward(self.pasos)
    
    def aumentarVelocidad(self):
        self.pasos += self.velocidad
    
    def crear(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            position = (random.randint(-250,250))
            autos = Turtle()
            autos.shape("square")
            autos.color(self.colorRandom())
            autos.penup()
            autos.goto(x=380,y=position)
            autos.shapesize(stretch_wid=1, stretch_len=2)
            self.lista_autos.append(autos)
