from point_line import Point, Line


class Cell:
    def __init__(self, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = window

    def draw(self, x1, x2, y1, y2):
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

        if self.has_left_wall:
            self.__win.draw_line(line_left, "black")

        if self.has_top_wall:
            self.__win.draw_line(line_top, "black")

        if self.has_right_wall:
            self.__win.draw_line(line_right, "black")

        if self.has_bottom_wall:
            self.__win.draw_line(line_bottom, "black")
