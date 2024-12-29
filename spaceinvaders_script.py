import turtle
import time
import random

window_object= turtle.Screen()
window_object.title("SPACE INVADERS")
window_object.bgcolor("black")
window_object.setup(width=600, height=600)
window_object.tracer(0) #to switch off the auto update feature

#Borders
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("green")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()    
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

score =0

#scoreboard
scoreboard = turtle.Turtle()
scoreboard.speed(0)
scoreboard.color("white")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(0, 260)
scoreboard.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))

#player
player = turtle.Turtle()
player.shape("square")
player.color("blue")
player.shapesize(stretch_wid=1, stretch_len=2)
player.penup()
player.goto(0, -250)

#bullet
bullet = turtle.Turtle()
bullet.shape("square")
bullet.color("yellow")
bullet.shapesize(stretch_wid=0.5, stretch_len=1)
bullet.penup()
bullet.goto(0, -400)
bullet.hideturtle()

global bullet_state, alienspeed
playerspeed= 15
aliens=[]
alienspeed= 5 
bullet_state = "ready"  # "ready" means the bullet is not visible, "fire" means it's visible

for alien in range(5):
    alien = turtle.Turtle()
    alien.shape("turtle")
    alien.color("red")
    alien.penup()
    alien.speed(0)
    x = random.randint(-350, 350)
    y = random.randint(100, 250)
    alien.goto(x, y)
    aliens.append(alien)

#movement
def move_left():
    x = player.xcor()
    if x > -380:
        player.setx(x - playerspeed)

def move_right():
    x = player.xcor()
    if x < 380:
        player.setx(x + playerspeed)

# function to control a bullet
def fire_bullet():
    global bullet_state
    if bullet_state == "ready":
        bullet_state = "fire"
        bullet.goto(player.xcor(), player.ycor() + 10)
        bullet.showturtle()

def move_bullet():
    global bullet_state
    if bullet_state == "fire":
        y = bullet.ycor()
        bullet.sety(y + 20)

    # hide bullet when it goes outside screen area
    if bullet.ycor() > 300:
        bullet.hideturtle()
        bullet_state = "ready"

def move_aliens():
    global alienspeed
    for alien in aliens:
        x = alien.xcor()
        alien.setx(x + alienspeed)

        # Move the alien down when it hits the screen edge
        if alien.xcor() > 370 or alien.xcor() < -370:
            for a in aliens:
                y = a.ycor()
                a.sety(y - 20)
            alienspeed *= -1
            break

# Function to check for collision with alien
def check_collision():
    global bullet_state
    for alien in aliens:
        if bullet.distance(alien) < 20:
            alien.goto(random.randint(-350, 350), random.randint(100, 250))  # Reset the alien position
            bullet.hideturtle()
            bullet_state = "ready"
            return True
    return False

# Function to check if alien reaches the player
def check_game_over():
    for alien in aliens:
        if alien.ycor() < -240:
            return True
    return False


# Keyboard bindings
window_object.listen()
window_object.onkey(move_left, "Left")
window_object.onkey(move_right, "Right")
window_object.onkey(fire_bullet, "space")

while True:
    move_bullet()
    move_aliens()
    if check_collision():
        pass  
    if check_game_over():
        print("Game Over!")
        time.sleep(1)
        window_object.bye()
    window_object.update()
    time.sleep(0.02)




window_object.mainloop()