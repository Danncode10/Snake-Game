from shutil import which
from tkinter.constants import RIGHT
from turtle import Turtle

# from main import whole_body

# Global Variable
STARTING_POSITION = [(0,0), (-20,0), (-40,0)]
DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake():

    def __init__(self):
        self.whole_body = []
        self.create_snake()
        self.head = self.whole_body[0]

    def create_snake(self):
        # global whole_body
        for position in STARTING_POSITION:
            new_segment = Turtle(shape="square")
            new_segment.penup()  # para walang trail ng lines
            new_segment.color("white")
            new_segment.goto(position)
            self.whole_body.append(new_segment)

    def move(self):
        for i in range(len(self.whole_body) - 1, 0, -1):
            new_x = self.whole_body[i - 1].xcor()
            new_y = self.whole_body[i - 1].ycor()
            self.whole_body[i].goto(new_x, new_y)
        # Move the head by 20,
        self.head.forward(DISTANCE)

    def controls(self, screen):
        screen.listen()
        screen.onkey(self.up, "Up")
        screen.onkey(self.down, "Down")
        screen.onkey(self.left, "Left")
        screen.onkey(self.rigth, "Right")

    def direction(self, degree):
        if(not(self.head.heading() == degree + 180 or self.head.heading() == degree - 180)): #Dont allow snake to move to its opposite
            self.head.setheading(degree)

    def up(self):
        self.direction(UP)

    def down(self):
        self.direction(DOWN)

    def left(self):
        self.direction(LEFT)

    def rigth(self):
        self.direction(RIGHT)

    def add_size(self):
        new_segment = Turtle(shape="square")
        new_segment.penup()  # para walang trail ng lines
        new_segment.color("white")

        last_segment = self.whole_body[len(self.whole_body) - 1]
        x = last_segment.xcor()
        y = last_segment.ycor()

        new_segment.goto(x,y)
        self.whole_body.append(new_segment)