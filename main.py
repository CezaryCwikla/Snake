from turtle import Screen
from snake import Snake
from food import Food
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.listen()
screen.tracer(0)
snake = Snake()
food = Food()

screen.onkey(fun=snake.turn_left, key="a")
screen.onkey(fun=snake.turn_right, key="d")


while -300 < snake.first_turtle.xcor() < 300 and -300 < snake.first_turtle.ycor() < 300:
    snake.move()
    screen.update()
    time.sleep(0.1)

    if food.distance(snake.first_turtle.position()) < 15:
        food.refresh()










screen.exitonclick()