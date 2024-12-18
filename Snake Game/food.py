from turtle import Turtle
import random as r

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("red")
        self.speed("fastest") #para mabilis ung animation, ndi na mag start sa (0,0)
        self.new_location()

    def new_location(self):
        x = r.randint(-280, 280)
        y = r.randint(-280, 280)
        self.goto(x, y)
