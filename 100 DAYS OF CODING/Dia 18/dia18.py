# import colorgram
from turtle import Turtle, Screen
import random
# rgb_colors = []
# color = colorgram.extract('image.jpg',30)
# for colo in color:
#     r = colo.rgb.r
#     g = colo.rgb.g
#     b = colo.rgb.b
#     tupla_colores = (r,g,b)
#     rgb_colors.append(tupla_colores)

rgb_colors = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
[(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

melman = Turtle()
screen = Screen().colormode(255)
melman.penup()
melman.setheading(225)
melman.forward(300)
melman.setheading(0)
posx = melman.xcor()
pos = melman.ycor()
for n in range(10):
    for n in range(10):
        melman.dot(20, random.choice(rgb_colors))
        melman.pendown()
        melman.penup()
        melman.forward(50)
    pos += 50
    melman.sety(pos)
    melman.setx(posx)
    
    



screen = Screen()
screen.exitonclick()



