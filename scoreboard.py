from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.setposition(x=-290, y=260)
        self.level = 1
        self.write_level()

    def increase_level(self):
        self.level += 1
        self.write_level()

    def write_level(self):
        self.clear()
        level_text = f"Level: {self.level}"
        self.write(level_text, font=FONT)

    def write_game_over(self):
        self.goto(-75, 0)
        self.write("GAME OVER", font=FONT)

