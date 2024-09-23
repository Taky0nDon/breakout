import turtle as t

class Ball(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")

    def move_ball(self, x_change: int, y_change: int):
        self.goto(self.pos() + (x_change, y_change))
