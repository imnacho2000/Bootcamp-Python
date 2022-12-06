from turtle import Screen 
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Snake Game by Nachota")

screen.listen()
snake = Snake()
food = Food()
score = ScoreBoard()

screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    snake.move()
    if(snake.cabeza.distance(food) < 15):
        food.mover()
        score.aumentar()
        snake.actualizar()
    if((snake.cabeza.xcor() > 280) | (snake.cabeza.xcor() < -280) | (snake.cabeza.ycor() > 280) | (snake.cabeza.ycor() < -280)):
        score.reset()
        snake.reset()
    for cuerpo in snake.cuerpo_snake[1:]:
        if snake.cabeza.distance(cuerpo) < 10:
            score.reset() 
            snake.reset()


screen.exitonclick()