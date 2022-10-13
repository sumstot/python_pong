from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setposition(0, 0)
        self.x_move = 3
        self.y_move = 3

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def bounce_paddle(self):
        if self.x_move < 0:
            self.x_move -= .5
        else:
            self.x_move += .5
        if self.y_move < 0:
            self.y_move -= .5
        else:
            self.y_move += .5
        self.x_move *= -1

    def reset(self):
        self.setposition(0, 0)
        self.x_move *= -1

    def speed_reset(self):
        self.x_move = 3
        self.y_move = 3
