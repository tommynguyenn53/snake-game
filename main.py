from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # Turn off automatic screen updates

# Create game objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Control the snake using arrow keys
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Start the game loop
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)  # Delay for smoother movement
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or \
       snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()

    # Detect collision with self (tail)
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()

screen.exitonclick()  # Exit on click
