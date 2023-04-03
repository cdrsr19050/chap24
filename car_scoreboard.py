from turtle import Turtle
from turtle import Screen
screen = Screen()

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.penup()
        self.ht()
        self.goto(0,270)
        self.update_score()
        #self.st()                     

    def update_score(self):
        self.write(f"Score is {self.score}",move=False,align="center",font=('Arial',12,'bold'))

    def end_game(self):
        self.goto(0,0)
        self.write("Game is over!",move=False,align="center",font=('Arial',12,'bold'))
        screen.bye()

    def increase_score(self):         
        self.score +=1   
        self.clear()   
        self.update_score()