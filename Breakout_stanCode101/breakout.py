"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
from campy.gui.events.mouse import onmouseclicked
from campy.gui.events.mouse import onmousemoved

FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3			 # Number of attempts
RUN = True


def main():
    graphics = BreakoutGraphics()

    # Add the animation loop here!
    window = graphics.window
    ball = graphics.ball
    dx = graphics.get_dx()
    dy = graphics.get_dy()
    num_lives = NUM_LIVES
    init_y_speed = graphics.get_init_y_speed()
    num_bricks = graphics.get_number_of_bricks()
    while num_lives > 0 and num_bricks > 0:
        pause(FRAME_RATE)
        if graphics.starting:
            ball.move(dx, dy)
            ball_points = [(ball.x, ball.y), (ball.x + ball.width, ball.y),
                           (ball.x, ball.y + ball.width), (ball.x + ball.width, ball.y + ball.width)]
            for ball_point in ball_points:
                ball_x, ball_y = ball_point
                obj = window.get_object_at(ball.x, ball.y)
                if obj is not None:
                    break
            if obj is not None:
                if obj is graphics.paddle:
                    dy = -init_y_speed
                else:
                    window.remove(obj)
                    dy = -dy
                    num_bricks -= 1

            if ball.y < 0:
                dy = -dy
            if ball.x + ball.width > window.width or ball.x < 0:
                dx = -dx
            if ball.y + ball.height > window.height:
                num_lives -= 1
                graphics.starting = False
                window.add(ball, x=(window.width - ball.width / 2) / 2, y=(window.height - ball.width / 2) / 2)
                dx = graphics.get_dx()


if __name__ == '__main__':
    main()
