from turtle import Turtle, Screen
from paddle import Paddle
screen = Screen()
screen.setup(width=800, height=600)
screen.title('Pong')
screen.bgcolor('black')
screen.tracer(0)

l_paddle = Paddle((350, 0))
r_paddle = Paddle((-350, 0))





screen.listen()
screen.onkey(l_paddle.up,'Up')
screen.onkey(l_paddle.down,'Down')
screen.onkey(r_paddle.up,'w')
screen.onkey(r_paddle.down,'s')




game_is_on = True

while game_is_on:
    screen.update()
screen.exitonclick()