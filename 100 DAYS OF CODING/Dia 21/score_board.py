from turtle import Turtle
text = ('arial',50,'normal')
position_score_uno = (-80,320)
position_score_dos = (40,320)
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score1 = 0
        self.score2 = 0
        self.id_uno = 1
        self.id_dos = 2
        self.hideturtle()
        self.penup()
        self.color("white")
        self.actualizar()
    
    def actualizar(self):
        self.goto(position_score_uno)
        self.write(f"{self.score1}",font=text)
        self.goto(position_score_dos)
        self.write(f"{self.score2}",font=text)
    
    def aumentarDos(self):
        self.score2 +=1
        self.clear()
        self.actualizar()
    
    def aumentarUno(self):
        self.score1 +=1
        self.clear()
        self.actualizar()
    
    def game_over(self,cantidad_goles):
        self.clear()
        self.goto(0,0)
        self.write(f"GAME OVER",align="center",font=text)
        self.goto(x=0,y=-20)
        if(self.score1 == cantidad_goles):
            self.write(f"GANO JUGADOR {self.id_uno} CON {self.score1} PUNTOS.",align="center",font=('Arial',20,'normal'))
        else:
            self.write(f"GANO JUGADOR {self.id_dos} CON {self.score2} PUNTOS.",align="center",font=('Arial',20,'normal'))