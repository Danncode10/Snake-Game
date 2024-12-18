from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()

        self.color("white")
        self.score = -2 # Nag ii start kasi ung program na Score: 2
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.add_score()
        self.score += 1
        self.show_score()

    def add_score(self):
        self.score += 1

    def show_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.color("red")
        self.show_score()

        self.goto(0,0)
        self.write(f"GAME OVER !", align=ALIGNMENT, font=FONT)
