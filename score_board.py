from turtle import Turtle

FONT = ("Courier", 18, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.update_score()

    def increase_level(self):
        self.level += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"level: {self.level}", align="left", font=FONT)

    def print_game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
