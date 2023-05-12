"""Import turtle library"""
from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)
    """function set up the movment for the turtle"""
    def go_up(self):
        self.forward(MOVE_DISTANCE)
    """function set up the starting position of the turtle"""
    def go_to_start(self):
        self.goto(STARTING_POSITION)
    """"""function determin if the turtle has reach the finish line"""
    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
