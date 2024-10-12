import turtle as t
from math import floor
from Paddle import Paddle
from Bricks import Brick

class Ball(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.speed(1)
        self.seth(270)
        self.x_change = 0
        self.y_change = -0.9

    def move_ball(self):
        self.forward(1)
        # self.goto(0, self.pos()[1] + self.y_change)

    def collided_with_paddle(self, other: Brick | Paddle):
        ball_y = self.pos()[1]
        other_y = other.pos()[1]
        min_distance = 20  # 10px ball radius + 5 px 0.5 paddle height
        distance = ball_y - other_y
        if int(distance) < min_distance:
            print("Collision detected")
            return True

    def collided_with_brick(self, other: Brick):
        vert_dist = self.pos()[1] - other.bottom_edge
        if vert_dist < 0:
            vert_dist *= -1
        in_horiz_bounds = self.pos()[0] > other.left_edge\
                and self.pos()[0] < other.right_edge
        vertical_collision = vert_dist < 10
        if vertical_collision and in_horiz_bounds:
            return True
        
    def bounce_back(self, direction):
        dir_heading_map = {
                "up": 90,
                "down": 270,
                "left": 135,
                "right": 45,
                }
        print(f"{self.heading()=}")
        self.change_heading(dir_heading_map[direction])

    def change_heading(self, new_h):
        self.speed(0)
        self.seth(new_h) 
        self.speed(1)
