from turtle import Turtle,Screen
import time

pasos = 20
arriba = 90
abajo = 270
derecha = 0
izquierda = 180
positions = [(0,0), (-20,0), (-40, 0)]

class Snake:
    def __init__(self):
        self.cuerpo_snake = []
        self.screen = Screen()
        self.crear()
        self.cabeza = self.cuerpo_snake[0]
        self.times = time
    
    def crear(self):
        for n in positions:
            self.agrandar(n)

    
    def move(self):
            self.screen.update()
            self.times.sleep(0.1)
            for n in range(len(self.cuerpo_snake)-1,0,-1):
                self.cuerpo_snake[n].goto(x= self.cuerpo_snake[n-1].xcor(),y=self.cuerpo_snake[n-1].ycor())
            self.cabeza.forward(pasos) 

    def up(self):
        if self.cabeza.heading() != abajo:
            self.cabeza.setheading(arriba)

    def down(self):
        if self.cabeza.heading() != arriba:
            self.cabeza.setheading(abajo)

    
    def right(self):
        if self.cabeza.heading() != izquierda:
            self.cabeza.setheading(derecha)

    
    def left(self):
        if self.cabeza.heading() != derecha:
            self.cabeza.setheading(izquierda)

    def agrandar(self, pos):
            snake = Turtle()
            snake.color("white")
            snake.shape("square")
            snake.penup()
            snake.goto(pos)
            self.cuerpo_snake.append(snake)
    
    def actualizar(self):
        self.agrandar(self.cuerpo_snake[-1].position())
    
    def reset(self):
        for cuerpo in self.cuerpo_snake:
            cuerpo.goto(x=1000,y=1000)
        self.cuerpo_snake.clear()
        self.crear()
        self.cabeza = self.cuerpo_snake[0]
