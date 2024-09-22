import turtle as t

MARGIN = 0.95
BOTTOM_MARGIN = 0.8
class Board():
    def __init__(self):
        self.screen = t.Screen()
        self.screen.bgcolor("red")
        self.width = self.screen.window_width()
        self.height = self.screen.window_height()
        self.upper_edge = self.height/2 * MARGIN
        self.right_edge = self.width/2 * MARGIN
        self.left_edge = self.right_edge * -1
        self.bottom = self.height/-2*BOTTOM_MARGIN
        self.start_listening_for_keys()

    def start_listening_for_keys(self):
        self.screen.listen()
        self.screen.onkey(fun=quit, key="q")

