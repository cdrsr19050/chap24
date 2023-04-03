from turtle import Turtle
import random
COLORS = ["red", "blue", "green", "orange", "yellow"]

class Car_Management():
    def __init__(self):
        self.all_cars = []
                       
    def new_car(self):  
        random_choice = random.randint(1,6)
        if random_choice == 1:
            new_car = Turtle("square")
            new_car.penup() 
            new_car.ht()
            new_car.shapesize(1,2)        
            new_car.seth(180)
            new_car.color(random.choice(COLORS))
            new_y = random.randint(-220,220)
            new_car.goto(300, new_y)
            self.all_cars.append(new_car)
            new_car.showturtle()        

    def move(self):
        for c in self.all_cars:   
            c.forward(5)



        