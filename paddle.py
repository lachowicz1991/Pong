from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, y_x):
        super().__init__()
        paddle = Turtle(shape='square')
        paddle.color('white')
        paddle.shapesize(stretch_len=1, stretch_wid=5)
        paddle.penup()
        self.goto(y_x)



    def up(self):
        new_y = self.ycor() +20
        print('up')
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() -20
        self.goto(self.xcor(), new_y)
    #
    # def down(self):
    #     self.paddle.setheading(DOWN)
