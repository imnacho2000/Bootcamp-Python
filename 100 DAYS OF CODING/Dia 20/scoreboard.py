from turtle import Turtle
alineamiento = "center"
font = ('Arial',15,'normal')
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x=-10, y=270)
        self.hideturtle()
        self.actualizar()

    def actualizar(self):
        self.write(f"Puntuacion: {self.score}", align=alineamiento, font = font)
    
    def aumentar(self):
        self.score += 1
        self.clear()
        self.actualizar()
    
    def game_over(self):
        self.clear()
        self.goto(x=0,y=0)
        self.write(f"GAME OVER", align=alineamiento, font = ('Arial',30,'normal'))
        self.goto(x=0,y=-20)
        self.actualizar()
        