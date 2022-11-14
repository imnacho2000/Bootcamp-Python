from score_board import ScoreBoard
from pong_body import PongBody
from ball import Ball
import time
from turtle import Screen

ball = Ball()

screen = Screen()
screen.setup(width=1200, height=800)
screen.bgcolor("black")
screen.title("ping pong by Nachota")
screen.tracer(0)

cantidad_goles = int(screen.textinput(f"A JUGAR MARICAS","A cuantos goles quieres jugar?"))


score = ScoreBoard()


position_uno = (-580, 0)
position_dos = (580, 0)

jugador_uno = PongBody(position_uno)
jugador_dos = PongBody(position_dos)

screen.listen()

screen.onkey(jugador_uno.up,"Up")
screen.onkey(jugador_uno.down,"Down")

screen.onkey(jugador_dos.up,"w")
screen.onkey(jugador_dos.down,"s")

game_is_on = True
while game_is_on:
    time.sleep(ball.gol)
    screen.update()
    ball.mover() 
    if((ball.ycor() > 370)  | (ball.ycor() < -370)):
        ball.reboteY()
    if (((ball.distance(jugador_dos) < 50) and (ball.xcor() > 540)) | ((ball.distance(jugador_uno) < 50) and (ball.xcor() < -540))):
        ball.reboteX()
    if (ball.xcor() > 580):
        score.aumentarUno()
        ball.medio()
    elif(ball.xcor() < -580):
        score.aumentarDos()
        ball.medio()
    if(score.score1 == cantidad_goles):
        game_is_on=False
        score.game_over(cantidad_goles)
    elif(score.score2 == cantidad_goles):
        game_is_on=False
        score.game_over(cantidad_goles)

screen.exitonclick()