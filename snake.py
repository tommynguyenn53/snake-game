from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]  # Initial snake body positions
MOVE_DISTANCE = 20  # Distance each segment moves
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

# The Snake class handles movement, growth, and direction changes
class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]  # Reference to the head of the snake

    # Create the initial snake
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    # Add a new segment to the snake
    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    # Add a new segment at the tail (on food collision)
    def extend(self):
        self.add_segment(self.segments[-1].position())

    # Move the snake forward by moving segments to the position of the one ahead
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    # Turn up, down, left, right – ignore 180-degree turns
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
