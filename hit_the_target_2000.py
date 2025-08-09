import turtle
import random

ball_x_velocity = 3
ball_y_velocity = 3
gravity = -0.05
ball_in_motion = False  # starting state

screen = turtle.Screen()
screen.setup(600, 800)
screen.tracer(0)

cannon = turtle.Turtle()
cannon.shape("triangle")
cannon.color("green")
cannon.penup()
cannon.setposition(-150, 0)
cannon.setheading(45)

target = turtle.Turtle()
target.shape("circle")
target.color("blue")
target.penup()
def relocate_target():
    target.setposition(random.randint(50, 250), random.randint(-200, 200))
relocate_target()

ball = turtle.Turtle()
ball.shape("circle")
ball.turtlesize(0.5)
ball.color("firebrick")
ball.penup()
ball.setposition(cannon.position())

def shoot():
    global ball_in_motion, ball_x_velocity, ball_y_velocity
    if not ball_in_motion:
        ball_in_motion = True
        ball.setposition(cannon.position())
        ball_x_velocity = 3
        ball_y_velocity = 3

def move_left():
    cannon.setx(cannon.xcor() - 10)
    if not ball_in_motion:
        ball.setposition(cannon.position())

screen.onkey(shoot, "space")
screen.onkey(move_left, "Left")
screen.listen()

while True:
    if ball_in_motion:
        ball.setx(ball.xcor() + ball_x_velocity)
        ball.sety(ball.ycor() + ball_y_velocity)
        ball_y_velocity += gravity

        if ball.distance(target) < 20:
            relocate_target()
            ball_in_motion = False

    screen.update()

turtle.done()
