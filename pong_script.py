import os
import turtle 


window_object= turtle.Screen()
window_object.title("PONG GAME")
window_object.bgcolor("black")
window_object.setup(width=800, height=600)
window_object.tracer(0) #to switch off the auto update feature

score_a=0
score_b=0

#paddles and ball objects
paddle1=turtle.Turtle()
paddle2=turtle.Turtle()
paddle1.speed(0)
paddle2.speed(0)
paddle1.shape("square")
paddle2.shape("square")
paddle1.color("white")
paddle2.color("white")
paddle1.shapesize(stretch_wid=5, stretch_len=1)
paddle2.shapesize(stretch_wid=5, stretch_len=1)
paddle1.penup()
paddle2.penup()
paddle1.goto(-350,0)
paddle2.goto(350,0)

ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0,0)
ball.dx = 2
ball.dy = -2


# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("gray")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Algerian", 22, "normal"))

#paddle movement functions
def paddle1_up():
    y=paddle1.ycor()
    y+=20
    paddle1.sety(y)

def paddle1_down():
    y=paddle1.ycor()
    y-=20
    paddle1.sety(y)

def paddle2_up():
    y=paddle2.ycor()
    y+=20
    paddle2.sety(y)

def paddle2_down():
    y=paddle2.ycor()
    y-=20
    paddle2.sety(y)


#keyboard bindings
window_object.listen()
window_object.onkeypress(paddle1_up, "w")
window_object.onkeypress(paddle1_down, "s")
window_object.onkeypress(paddle2_up, "Up")
window_object.onkeypress(paddle2_down, "Down")


#gameloop
while True:
    window_object.update()

    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #reversing direction in case it hits the top and bottom borders
    if ball.ycor() > 290 :
        ball.sety(290)
        ball.dy*= -1
        os.system("afplay bounce.wav&")

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("afplay bounce.wav&")
    
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle2.ycor() + 40 and ball.ycor() > paddle2.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
        os.system("afplay bounce.wav&") #play bounce.wav sound effect

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle1.ycor() + 40 and ball.ycor() > paddle1.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
        os.system("afplay bounce.wav&")

    #computer play
    if paddle2.ycor() < ball.ycor() and abs(paddle2.ycor() - ball.ycor()) > 10:
        paddle2_up()

    elif paddle2.ycor() > ball.ycor() and abs(paddle2.ycor() - ball.ycor()) > 10:
        paddle2_down()