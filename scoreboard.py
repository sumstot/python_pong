from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 30, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.penup()
        self.hideturtle()
        self.setposition(0, 260)
        self.color("white")
        self.write(f"{self.l_score}   :   {self.r_score}", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.clear()

    def increase_left_score(self):
        self.l_score += 1
        self.write(f"{self.l_score}   :   {self.r_score}", align=ALIGNMENT, font=FONT)

    def increase_right_score(self):
        self.r_score += 1
        self.write(f"{self.l_score}   :   {self.r_score}", align=ALIGNMENT, font=FONT)