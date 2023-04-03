from turtle import Screen
from myturtle import MyTurtle
from car_management import Car_Management
from car_scoreboard import Scoreboard

import time 

myturtle = MyTurtle()
car_management = Car_Management()
scoreboard = Scoreboard()


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Turtle crossing game")
screen.tracer(0)

screen.listen()
screen.onkeypress(myturtle.move_up,"Up")
screen.onkeypress(myturtle.move_back,"Down")
keep_moving = True


while keep_moving:
    screen.update()
    time.sleep(.01)
    car_management.new_car()
    car_management.move()

    for car in car_management.all_cars:
        # pass
        if myturtle.distance(car) < 20:
            keep_moving = False

    
    if myturtle.ycor() > 280:
        scoreboard.increase_score()
        myturtle.start()



screen.exitonclick()