from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(270)
        self.shape("square")
        self.shapesize(stretch_wid=2, stretch_len=1)
        self.color(random.choice(COLORS))
        self.setposition(x=320, y=random.randint(-250, 250))

    def move(self, speed):
        new_x = self.xcor() - speed
        self.goto(new_x, self.ycor())

