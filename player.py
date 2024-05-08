from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.go_to_start_position()

    def move_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def go_to_start_position(self):
        self.setposition(STARTING_POSITION)
        self.setheading(90)

    # Detect player win level
    def check_if_player_reached_end(self):
        if self.ycor() == FINISH_LINE_Y:
            return True
        else:
            return False
