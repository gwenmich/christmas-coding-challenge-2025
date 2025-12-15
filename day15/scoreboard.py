from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setposition(0, 270)
        self.score = 0
        self.update()

    def update(self):
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)
