from turtle import Turtle

posInicial = (0,-280)
pasos = 10

class Tortuga(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.goto(posInicial)


    def posInicial(self):
        if(self.ycor() > 290):
            return True
        return False

    def mover(self):
        self.forward(pasos)
    
    def abajo(self):
        self.backward(pasos)
    
    def ini(self):
        self.goto(posInicial)
    
    