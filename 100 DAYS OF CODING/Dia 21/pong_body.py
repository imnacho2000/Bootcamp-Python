from turtle import Turtle
class PongBody(Turtle):
    def __init__(self, positions):
        super().__init__()
        self.positions = positions
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(self.positions)

    def up(self):
        if(self.ycor() < 350):
            newy = self.ycor() + 20
            self.goto(x=self.positions[0], y=newy)

    def down(self):
        if(self.ycor() > -350):
            newy = self.ycor() - 20
            self.goto(x=self.positions[0], y=newy)


    

