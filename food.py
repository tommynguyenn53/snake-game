from turtle import Turtle
import random

# The Food class creates the food object that the snake can "eat"
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")  # Shape of the food
        self.penup()  # Don't draw lines when moving
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # Make it smaller
        self.color("blue")  # Color of the food
        self.speed("fastest")  # Max speed to avoid visual lag
        self.refresh()  # Place it at a random location

    # Moves the food to a new random location on the screen
    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
