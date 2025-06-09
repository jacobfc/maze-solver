from point_line import Point, Line

wall_color = "black"
empty_color = "#d9d9d9"


class Cell:
    def __init__(self, window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = window

        # Track whether the cell has been visited by wall-breaking algorithm
        self.visited_during_generation = False

        # Track whether the cell has been visited by the maze solver
        self.visited_during_solving = False

    def draw(self, x1, x2, y1, y2):
        # TODO: assert that x1 < x2, and y1 < y2?
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2

        # points and lines
        p1 = Point(x1, y1)
        p2 = Point(x2, y1)
        p3 = Point(x1, y2)
        p4 = Point(x2, y2)

        line_top = Line(p1, p2)  # top == y1
        line_bottom = Line(p3, p4)  # bottom == y2
        line_left = Line(p1, p3)  # left == x1
        line_right = Line(p2, p4)  # right == x2

        if self.__win is not None:  # only draw lines if a window is provided
            # left
            if self.has_left_wall:
                line_color = wall_color
            else:
                line_color = empty_color

            self.__win.draw_line(line_left, line_color)

            # top
            if self.has_top_wall:
                line_color = wall_color
            else:
                line_color = empty_color

            self.__win.draw_line(line_top, line_color)

            # right
            if self.has_right_wall:
                line_color = wall_color
            else:
                line_color = empty_color

            self.__win.draw_line(line_right, line_color)

            # bottom
            if self.has_bottom_wall:
                line_color = wall_color
            else:
                line_color = empty_color

            self.__win.draw_line(line_bottom, line_color)

    def draw_move(self, to_cell, undo=False):
        # draws a line from the center of 1 cell, to the center of another cell

        # find center of self and to_cell
        self_x_center = abs(self.__x1 + self.__x2) / 2
        self_y_center = abs(self.__y1 + self.__y2) / 2
        self_center_point = Point(self_x_center, self_y_center)

        other_x_center = (to_cell.__x1 + to_cell.__x2) / 2
        other_y_center = (to_cell.__y1 + to_cell.__y2) / 2
        other_center_point = Point(other_x_center, other_y_center)

        # create line from center points
        centers_line = Line(self_center_point, other_center_point)

        line_color = "red"
        if undo:
            line_color = "grey"

        if self.__win is not None:  # only draw lines if a window is provided
            self.__win.draw_line(centers_line, line_color)
