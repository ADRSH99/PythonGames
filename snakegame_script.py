import turtle
import time
import random

delay = 0.1

#score 
score = 0
high_score =0


window_object= turtle.Screen()
window_object.title("SNAKE GAME")
window_object.bgcolor("black")
window_object.setup(width=620, height=620)
window_object.tracer(0) #to switch off the auto update feature

#descrbing the snake head
snake_head=turtle.Turtle()
snake_head.speed(0)
snake_head.shape("circle")
snake_head.color("white")
snake_head.penup() #no trail on the screen
snake_head.direction ="stop" #no movement on kickoff

#describing the snake food
food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup() #no trail on the screen
food.goto(0,100)

segments=[]

#writing down the score
pen= turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("red")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("SCORE: 0 HIGH SCORE: 0", align="center", font=("Algerian", 18 ,"bold"))

#functions for movement
def move():
    if snake_head.direction =="up":
        y=snake_head.ycor()
        snake_head.sety(y+20)
    if snake_head.direction =="down":
        y=snake_head.ycor()
        snake_head.sety(y-20)
    if snake_head.direction =="left":
        x=snake_head.xcor()
        snake_head.setx(x-20)
    if snake_head.direction =="right":
        x=snake_head.xcor()
        snake_head.setx(x+20)

#functions for control and binidng keyboards 
def go_up():
    if snake_head.direction != "down":
        snake_head.direction="up"

def go_down():
    if snake_head.direction != "up":
        snake_head.direction="down"

def go_left():
    if snake_head.direction != "right":
        snake_head.direction="left"

def go_right():
    if snake_head.direction != "left":
        snake_head.direction="right"


window_object.listen()
window_object.onkeypress(go_up, "w")
window_object.onkeypress(go_down, "s")
window_object.onkeypress(go_left, "a")
window_object.onkeypress(go_right, "d")


#game loop
while True:
    window_object.update()
    #boundary collision checker
    if abs(snake_head.xcor())> 300 or abs(snake_head.ycor()) > 300:
        time.sleep(1)
        snake_head.goto(0,0)
        snake_head.direction = "stop"
        #hide dead snake segments
        for segment in segments:
            segment.goto(1000,1000)
        #delete extra segments every run
        segments.clear()
        #reset score
        score = 0
        delay = 0.1
        pen.clear()
        pen.write("SCORE : {} HIGH SCORE: {}".format(score, high_score), align="center", font=("Algerian", 18 ,"bold"))

    #food collision checker
    if snake_head.distance(food) < 20:
        #randomize the next food placement
        x= random.randint(-290,290)
        y= random.randint(-290, 290)
        food.goto(x,y)
        #add length/segment to snake
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)
        delay -=-0.001
        #add to score
        score+=1
        if score>high_score: 
            high_score= score
        pen.clear()
        pen.write("SCORE : {} HIGH SCORE: {}".format(score, high_score), align="center", font=("Algerian", 18 ,"bold"))


    #move the parts in an order
    for index in range (len(segments) - 1, 0 , -1):
        x=segments[index-1].xcor()
        y=segments[index-1].ycor()
        segments[index].goto(x,y)
    
    #to move segment in first postion behind head
    if len(segments) > 0:
        x= snake_head.xcor()
        y= snake_head.ycor()
        segments[0].goto(x,y)
    
    move()

    #snake head and body collision checker
    for segment in segments:
        if segment.distance(snake_head) < 20:
            time.sleep(1)
            snake_head.goto(0,0)
            snake_head.direction = "stop"

            #hide body after collision
            for segments in segments:
                segment.goto(1000,1000)
            segments.clear()

            score=0
            delay=0.1
            pen.clear()
            pen.write("SCORE : {} HIGH SCORE: {}".format(score, high_score), align="center", font=("Algerian", 18 ,"bold"))
    
    time.sleep(delay)



window_object.mainloop()