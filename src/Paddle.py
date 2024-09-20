import turtle as t


class Paddle(t.Turtle):
    def __init__(self, start_x: int|float , start_y: int|float):
        super().__init__()
        self.shape("square")
        self.shapesize(0.5, 2)
        self.penup()
        self.goto(start_x, start_y)
