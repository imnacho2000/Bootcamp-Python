from turtle import Turtle, Screen
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.gol = 0.1
        self.penup()
        self.screen = Screen()
        self.shapesize(stretch_wid=2)
        self.goto(0,0)
        self.x_move = 0
        self.y_move = 0
    
    def mover(self):
        self.goto(x=self.xcor() + self.x_move,y=self.ycor() + self.y_move)
    
    def reboteY(self):
        self.y_move *= -1
    
    def reboteX(self):
        self.x_move *= -1
        self.aumentarVelocidad()

    def medio(self):
        self.goto(x=0,y=0)
        self.gol = 0.1

    def aumentarVelocidad(self):
        self.gol *= 0.9
