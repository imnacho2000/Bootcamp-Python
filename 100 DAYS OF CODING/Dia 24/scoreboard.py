from turtle import Turtle
alineamiento = "center"
font = ('Arial',15,'normal')
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        with open("../../../../Escritorio/highscore.txt", mode="r") as file:
            self.highscore = int(file.read())  
        self.penup()
        self.goto(x=-20, y=270)
        self.hideturtle()
        self.actualizar()

    def actualizar(self):
        self.clear()
        self.write(f"Puntuacion: {self.score} Puntuacion maxima: {self.highscore}", align=alineamiento, font = font)
    
    def aumentar(self):
        self.score += 1
        self.actualizar()
    

    def reset(self):
        if(self.score > self.highscore):
            self.highscore = self.score  
        with open("../../../../Escritorio/highscore.txt", mode="w") as file:
            file.write(f"{self.highscore}")
        self.score = 0
        self.actualizar()
        