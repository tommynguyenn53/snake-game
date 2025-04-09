from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

# The Scoreboard class manages score display and high score tracking
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        # Load high score from file
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)  # Position at the top of the screen
        self.hideturtle()
        self.update_scoreboard()

    # Display current score and high score
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score {self.high_score}", align=ALIGNMENT, font=FONT)

    # Reset score and update high score if necessary
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    # Increase score by 1
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
