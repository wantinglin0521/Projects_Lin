"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Height of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Count bricks
        self.brick_rows = brick_rows
        self.brick_cols = brick_cols

        # Create a paddle
        self.paddle = GRect(width=paddle_width, height=paddle_height)
        self.paddle.filled = True
        self.paddle.fill_color = "black"
        self.window.add(self.paddle, x=(self.window.width-self.paddle.width)/2, y=(self.window.height-paddle_offset))

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.ball.fill_color = "gray"
        self.ball.color = "gray"
        self.window.add(self.ball, x=(self.window.width-ball_radius)/2, y=(self.window.height-ball_radius)/2)

        # Default initial velocity for the ball
        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED
        self.starting = False

        # Initialize our mouse listeners
        onmousemoved(self.paddle_move)
        onmouseclicked(self.start_moving)

        # Draw bricks
        brick_color = ["red", "red", "orange", "orange", "yellow", "yellow", "green", "green", "blue", "blue"]
        y_location = brick_offset
        for i in range(brick_rows):
            x_location = 0
            for j in range(brick_cols):
                self.brick = GRect(brick_width, brick_height, x=x_location, y=y_location)
                self.brick.filled = True
                self.brick.fill_color = brick_color[i]
                self.window.add(self.brick)
                x_location += brick_spacing + brick_width
            y_location += brick_spacing + brick_height

    def paddle_move(self, event):
        self.paddle.x = event.x - self.paddle.x/2
        if self.paddle.x < 0:
            self.paddle.x = 0
        if self.paddle.x + self.paddle.width > self.window.width:
            self.paddle.x = self.window.width - self.paddle.width

    def start_moving(self, event):
        if not self.starting:
            self.window.add(self.ball, x=(self.window.width - self.ball.width / 2) / 2,
                            y=(self.window.height - self.ball.width / 2) / 2)
            self.starting = True

    def get_dx(self):
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            return -self.__dx
        return self.__dx

    def get_dy(self):
        return self.__dy

    def get_init_y_speed(self):
        return INITIAL_Y_SPEED

    def get_number_of_bricks(self):
        return self.brick_rows*self.brick_cols


