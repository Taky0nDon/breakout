import turtle as t


class Paddle(t.Turtle):
    def __init__(self, start_x: int|float , start_y: int|float):
        super().__init__()
        self.shape("square")
        self.shapesize(0.5, 8)
        self.penup()
        self.goto(start_x, start_y)

    def move_right(self):
        current_x, current_y = self.pos()
        move_distance = 10
        new_x = current_x + move_distance
        self.goto(new_x, current_y)

    def move_left(self):
        current_x, current_y = self.pos()
        move_distance = -10
        new_x = current_x + move_distance
        self.goto(new_x, current_y)
