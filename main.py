from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from time import sleep
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=800, height=600)
screen.title('Pong')
screen.bgcolor('black')
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
mid_paddle = Ball()
scoreboard_pong = Scoreboard()
mid_paddle.move()


screen.listen()
screen.onkey(r_paddle.up, 'Up')
screen.onkey(r_paddle.down, 'Down')
screen.onkey(l_paddle.up, 'w')
screen.onkey(l_paddle.down, 's')




game_is_on = True

while game_is_on:
    mid_paddle.move()
    sleep(mid_paddle.tempo)
    screen.update()

    #Wall Collision
    if mid_paddle.ycor() >280 or mid_paddle.ycor() < -280:
        mid_paddle.bounce_y()


    if mid_paddle.distance(r_paddle) <50 and mid_paddle.xcor() > 320 or mid_paddle.distance(l_paddle) < 50 and mid_paddle.xcor() < -330:
        print('contact')
        mid_paddle.bounce_x()


    if mid_paddle.xcor() < -360:
        r_paddle.points += 1
        mid_paddle.reset()
        scoreboard_pong.r_score += 1
        scoreboard_pong.show()

    if mid_paddle.xcor() > 360:
        mid_paddle.reset()
        scoreboard_pong.l_score += 1
        scoreboard_pong.show()


screen.exitonclick()

