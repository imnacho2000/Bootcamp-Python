from turtle import Turtle

fonts = ('Arial',15,'normal') 
position_score = (-280,260)

class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.actualizar()
    
    def actualizar(self):
        self.goto(position_score)
        self.write(f"Nivel: {self.level}",font=fonts)
    
    def aumentar(self):
        self.level += 1
        self.clear()
        self.actualizar()
    
    def gameover(self):
        self.clear()
        self.goto(0,0)
        self.write(f"GAME OVER",align = "center",font=('Arial',50,'normal'))
        self.goto(x=-50,y=-20)
        self.write(f"Puntuacion: {self.level}",font=fonts)