from turtle import Turtle

MOVE_DISTANCE = 10
HEADING = 90
INITIAL_POSITION = (0, -280)
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(HEADING)
        self.penup()
        self.reset_to_initial_position()

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def reset_to_initial_position(self):
        self.goto(INITIAL_POSITION)
