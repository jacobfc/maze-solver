from window import Window
from point_line import Line, Point
from cell import Cell


def main():
    win = Window(800, 600)
    # win.wait_for_close()

    """
    point_1 = Point(20, 80)
    point_2 = Point(150, 180)
    point_3 = Point(150, 80)

    line1 = Line(point_1, point_2)
    line2 = Line(point_2, point_3)
    line3 = Line(point_3, point_1)

    win.draw_line(line1, "blue")
    win.draw_line(line2, "red")
    win.draw_line(line3, "green")
    """

    cell_1 = Cell(win)
    cell_1.has_left_wall = False
    cell_1.draw(20, 80, 150, 180)

    cell_2 = Cell(win)
    cell_2.draw(5, 10, 10, 15)

    # always comes last
    win.wait_for_close()


if __name__ == "__main__":
    main()
