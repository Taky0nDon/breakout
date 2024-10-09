import turtle as t
from math import floor
from Paddle import Paddle
from Bricks import Brick

class Ball(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.speed(1)
        self.x_change = 0
        self.y_change = -4

    def move_ball(self):
        self.goto(0, self.pos()[1] + self.y_change)

    def collided_with_paddle(self, other: Brick | Paddle):
        ball_y = self.pos()[1]
        other_y = other.pos()[1]
        min_distance = 10 + (floor(other.height_px) // 2)
        distance = ball_y - other_y
        print(distance)
        if int(distance) <= min_distance:
            print("Collision detected")
            return True

    def bounce_back(self):
        self.y_change *= -1
