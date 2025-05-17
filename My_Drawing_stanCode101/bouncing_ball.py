"""
File: bouncing_ball.py
Name:Vivian Lin
-------------------------
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
LIVE = 3
RUN = True

window = GWindow(800, 500, title='bouncing_ball.py')
oval = GOval(SIZE, SIZE, x=START_X, y=START_Y)


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    oval.filled = True
    oval.fill_color = "blue"
    oval.color = "blue"
    if LIVE > 0:
        window.add(oval, x=START_X, y=START_Y)
        onmouseclicked(switch)


def create_oval():
    global oval
    global RUN
    vx = VX
    vy = 0
    while oval.x <= window.width:
        if oval.y + SIZE/2 >= window.height:
            vy = -vy * REDUCE
            oval.move(vx, vy - SIZE/2)
        else:
            oval.move(vx, vy)
            pause(DELAY)
            vy += GRAVITY
    RUN = True
    window.add(oval, x=START_X, y=START_Y)


def switch(event):
    global LIVE
    global RUN
    if LIVE > 0 and RUN is True:
        RUN = False
        create_oval()
        LIVE -= 1


if __name__ == "__main__":
    main()
