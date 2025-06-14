from window import Window
from point_line import Line, Point
from cell import Cell
from maze import Maze


def main():
    win = Window(800, 600)

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

    """
    cell_1 = Cell(win)
    cell_1.has_left_wall = False
    cell_1.draw(20, 80, 150, 180)

    cell_2 = Cell(win)
    cell_2.draw(5, 10, 10, 15)

    cell_3 = Cell(win)
    cell_3.draw(100, 150, 100, 150)

    cell_1.draw_move(cell_2, undo=True)
    cell_2.draw_move(cell_3)
    """

    # maze = Maze(50, 50, 3, 3, 50, 50, win, sleep_timer=0.1, seed=0)
    # maze = Maze(50, 50, 12, 12, 15, 15, win, sleep_timer=0.1, seed=0)
    maze = Maze(20, 20, 30, 30, 8, 8, win, sleep_timer=0.01, seed=0)
    # always comes last
    win.wait_for_close()


if __name__ == "__main__":
    main()
