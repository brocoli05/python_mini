from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()   # an arrow disappear
        self.goto(0, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()  # avoid overlapping score
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def reset(self):
        """ if player hit the highest score then update the high score"""
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0  # reset the score
