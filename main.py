from scoreboard import Score
from turtle import Screen
from snake import Snake
from food import Food
import time


screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake-Game")
screen.tracer(0)


snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with wall
    if snake.first.xcor() > 300 or snake.first.xcor() < -300 or snake.first.ycor() > 300 or snake.first.ycor() < -300:
        score.reset_score()
        snake.se_pos()

    # detect collision of head with any tail
    for x in snake.inst[1:]:
        if snake.first.distance(x) < 10:
            score.reset_score()
            snake.se_pos()

    # collision with food
    if snake.first.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.inc_score()


