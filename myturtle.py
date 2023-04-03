from token import STAR
from turtle import Turtle
STARTING_POINT = (0,-270)


class MyTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.shape("turtle")
        self.color("black")
        self.penup()        
        self.seth(90)
        self.start()
        self.st()

    def move_up(self):
        self.forward(5)

    def move_back(self):
        self.backward(5)

    def start(self):
        self.goto(STARTING_POINT)

        
        