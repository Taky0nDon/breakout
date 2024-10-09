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
        self.y_change = -0.9

    def move_ball(self):
        self.goto(0, self.pos()[1] + self.y_change)

    def collided_with_paddle(self, other: Brick | Paddle):
        ball_y = self.pos()[1]
        other_y = other.pos()[1]
        min_distance = 15  # 10px ball radius + 5 px 0.5 paddle height
        distance = ball_y - other_y
        print(distance)
        if int(distance) <= min_distance:
            print("Collision detected")
            return True

    def collided_with_brick(self, other: Brick):
        vert_dist = self.pos()[1] - other.bottom_edge
        if vert_dist < 0:
            vert_dist *= -1
        in_horiz_bounds = self.pos()[0] > other.left_edge\
                and self.pos()[0] < other.right_edge
        vertical_collision = vert_dist < 10
        print(f"{other.pos()=}")
        print(f"{self.pos()=}")
        if vertical_collision and in_horiz_bounds:
            print(f"{other.bottom_edge=}")
            print(self.pos())
            print(f"{vert_dist=}")
            return True
        
    def bounce_back(self):
        self.y_change *= -1
