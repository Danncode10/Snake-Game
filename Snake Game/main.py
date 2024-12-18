from turtle import Screen
import time
from snake import Snake
import food
from scoreboard import ScoreBoard

def detect_wall_collision():
    global game_is_on
    if(snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290):
        score.game_over()
        game_is_on = False

def detect_tail_collison():
    global game_is_on
    for part in snake.whole_body: #Note that head is part of whole_body
        if part == snake.head:
            pass
        elif snake.head.distance(part) < 10:
            score.game_over()
            game_is_on = False

def food_collision():
        if snake.head.distance(eat) < 15: #15 kase between 20 and 10, size ng food at snake
            eat.new_location()
            snake.add_size()
            score.add_score()
            score.show_score()


def main():
    screen.update()
    snake.controls(screen) #allows user to control snake

    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        food_collision()
        detect_wall_collision()
        detect_tail_collison()


#Glabal Variables
screen = Screen()
snake = Snake()
score = ScoreBoard()
game_is_on = True
eat = food.Food()

#Configure screen
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

#CALL

main()
screen.mainloop()