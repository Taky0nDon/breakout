import turtle as t
from Board import Board
from Paddle import Paddle
from Ball import Ball
from Bricks import BrickManager, Brick


def setup(board: Board) -> Board:
    txt_writer = t.Turtle()
    txt_writer.hideturtle()
    txt_writer.penup()
    txt_writer.goto(board.left_edge, board.bottom)
    txt_writer.pendown()
    txt_writer.write("Press q to quit")
    board.screen.onkey(fun=quit, key="q")
    return board


def setup_paddle_control(paddle: Paddle):
    game_board.screen.onkey(fun=paddle.move_right, key="l")
    game_board.screen.onkey(fun=paddle.move_left, key="h")


game_board = setup(Board())
player = Paddle(start_x=0, start_y=game_board.bottom, board=game_board)
setup_paddle_control(player)
ball = Ball()
brick_manager = BrickManager()
brick_manager.build_bricks(n=4, board=game_board)
ball.forward(50)
game_being_played: bool = True
while game_being_played:
    ball.move_ball()
    ball_x, ball_y = ball.pos()
    if wall_hit := ball.collided_with_wall(game_board):
        ball.bounce_back(surface=wall_hit)
    if ball.collided_with_paddle(player):
        if ball_x < player.pos()[0] - 5:
            ball.change_heading(135)
        elif ball_x > player.pos()[0] + 5:
            ball.change_heading(45)
        else:
            ball.change_heading(90)
    if ball_y < game_board.bottom - 100:
        game_board.game_over()
        game_being_played = False
    for brick in brick_manager.bricks:
        brick_hit = ball.collided_with_brick(brick)
        if brick_hit:
            location = Brick.return_side_hit_by_ball(brick, ball)
            brick.ht()  # Brick disappears
            brick_manager.destroy_brick(brick)  # Brick object deleted.
            ball.bounce_back(location)


game_board.screen.exitonclick()
