"""
File: babygraphics.py
Name: Vivian Lin
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    number_of_years = len(YEARS)
    year_space = (width-2*GRAPH_MARGIN_SIZE)/number_of_years
    return GRAPH_MARGIN_SIZE + year_space*year_index


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #
    # left vertical
    canvas.create_line(GRAPH_MARGIN_SIZE, 0, GRAPH_MARGIN_SIZE, CANVAS_HEIGHT, width=LINE_WIDTH, fill="black")
    # right vertical
    canvas.create_line(CANVAS_WIDTH-GRAPH_MARGIN_SIZE, 0, CANVAS_WIDTH-GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT, width=LINE_WIDTH, fill="black")
    # up horizontal
    canvas.create_line(CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       GRAPH_MARGIN_SIZE, width=LINE_WIDTH, fill="black")
    # low horizontal
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, width=LINE_WIDTH, fill="black")
    # other vertical lines and years
    for i in range(len(YEARS)):
        x_location = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(x_location, 0, x_location, CANVAS_HEIGHT)
        canvas.create_text(x_location + TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=YEARS[i], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #
    for name in lookup_names:
        color = COLORS[lookup_names.index(name) % 4]
        x0_to_y0_lst = []
        # name ranking in 1000
        if name in name_data:
            for year in YEARS:
                # in 1000 ranking
                if str(year) in name_data[name]:
                    rank = name_data[name][str(year)]
                    x0 = get_x_coordinate(CANVAS_WIDTH, YEARS.index(year))
                    y0 = ((int(rank)-1)/MAX_RANK * (CANVAS_HEIGHT-2*GRAPH_MARGIN_SIZE)) + GRAPH_MARGIN_SIZE
                    name_text = name + "" + rank
                    canvas.create_text(x0 + TEXT_DX, y0, text=name_text, anchor=tkinter.SW, fill=color)
                # not in 1000 ranking
                else:
                    x0 = get_x_coordinate(CANVAS_WIDTH, YEARS.index(year))
                    y0 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                    name_text = name + "*"
                    canvas.create_text(x0 + TEXT_DX, y0, text=name_text, anchor=tkinter.SW, fill=color)
                x0_to_y0_lst.append((x0, y0))
            # draw lines
            for x0, y0 in x0_to_y0_lst:
                if x0_to_y0_lst.index((x0, y0)) == (len(x0_to_y0_lst) - 1):
                    break
                else:
                    x1, y1 = x0_to_y0_lst[x0_to_y0_lst.index((x0, y0)) + 1]
                    canvas.create_line(x0, y0, x1, y1, fill=color, width=LINE_WIDTH)
        # name ranking not in 1000
        else:
            print("Entered name no record!")


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
