import turtle as t
from Board import Board
from Paddle import Paddle
from Bricks import Brick


BASE_SPEED = 10

class Ball(t.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.speed(BASE_SPEED)
        self.seth(270)

    def move_ball(self):
        self.forward(3)

    def collided_with_paddle(self, other: Brick | Paddle) -> bool:
        ball_x, ball_y = self.pos()
        paddle_x, paddle_y = other.pos()
        min_distance = 20  # 10px ball radius + 5 px 0.5 paddle height
        distance = ball_y - paddle_y
        if ball_x < paddle_x + other.width_px // 2 and ball_x > paddle_x - other.width_px // 2:
            if int(distance) < min_distance:
                return True
        return False

    def collided_with_brick(self, other: Brick) -> bool: 
        ball_x, ball_y = self.pos()
        dist_from_ball_to_bottom = int(other.bottom_edge - ball_y)
        dist_from_ball_to_top = int(other.top_edge - ball_y)
        dist_from_ball_to_left = int(other.left_edge - ball_x)
        dist_from_ball_to_right = int(other.right_edge - ball_x)
        ball_in_horizontal_bounds = all([
            ball_x >= other.left_edge, ball_x <= other.right_edge
            ])
        ball_in_vertical_bounds = all([
            ball_y >= other.bottom_edge, ball_y <= other.top_edge
            ])
        hit_bottom =  dist_from_ball_to_bottom in range(0, 11) and ball_in_horizontal_bounds
        hit_top = dist_from_ball_to_top in range(-10,1) and ball_in_horizontal_bounds
        hit_left = dist_from_ball_to_left in range(-10, 11) and ball_in_vertical_bounds 
        hit_right = dist_from_ball_to_right in range(-10, 11) and ball_in_vertical_bounds 
        if any([hit_bottom, hit_top, hit_left, hit_right]):
            return True
        else:
            return False

    def collided_with_wall(self, board: Board) -> str:
        """ Returns a string representing which edge of the board the ball hit"""
        ball_x, ball_y = self.pos()
        if ball_x <= board.left_edge:
            return "L"
        if ball_x >= board.right_edge:
            return "R"
        if ball_y >= board.upper_edge:
            return "T"
        else:
            return ""

    def bounce_back(self, surface=''):
        print(surface)
        initial_heading = int(self.heading())

        left_wall_heading_change = {
                135: 45,
                225: 315,
                }

        right_wall_heading_change = {
                315: 225,
                45: 135,
                }

        ceiling_heading_change = {
                90: 270,
                45: 315,
                135: 225
                }

        brick_top_heading_change = {
                270: 90,
                315: 45,
                225: 135
                }

        brick_bottom_heading_change = ceiling_heading_change

        brick_left_heading_change = right_wall_heading_change
        brick_right_heading_change = left_wall_heading_change

        if surface in ["L" , "right"]:  # right of brick behaves like left wall 
            self.change_heading(
                    left_wall_heading_change[initial_heading]
                    )

        elif surface in ["R" , "left"]:  # left of brick behaves like right wall
            self.change_heading(
                    right_wall_heading_change[initial_heading]
                    )

        elif surface == "T":
            self.change_heading(
                    ceiling_heading_change[initial_heading]
                    )

        elif surface == "top":
            self.change_heading(
                    brick_top_heading_change[initial_heading]
                    )

        elif surface == "bottom":
            self.change_heading(
                    brick_bottom_heading_change[initial_heading]
                    )




    def change_heading(self, new_h: float):
        self.speed(0)
        self.seth(new_h)
        self.speed(BASE_SPEED)
