"""
File:draw_line.py
Name:Vivian Lin
-------------------------
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked
SIZE = 4
window = GWindow()
counter = 1
r = 0
s = 0


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw_oval)


def draw_oval(mouse):
    global counter
    global r
    global s
    # odd draw oval, even draw line
    if counter % 2 != 0:
        oval = GOval(SIZE, SIZE, x=mouse.x-SIZE/2, y=mouse.y-SIZE/2)
        oval.filled = False
        window.add(oval)
        r = mouse.x
        s = mouse.y
    else:
        remove_oval = window.get_object_at(r, s)
        line = GLine(x0=r, y0=s, x1=mouse.x, y1=mouse.y)
        window.add(line)
        window.remove(remove_oval)
    counter += 1


if __name__ == "__main__":
    main()
