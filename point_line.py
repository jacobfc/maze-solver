class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, point_a, point_b):
        self.point_a = point_a
        self.point_b = point_b

    def draw(self, canvas, fill_color):
        x1 = self.point_a.x
        x2 = self.point_b.x
        y1 = self.point_a.y
        y2 = self.point_b.y
        canvas.create_line(x1, y1, x2, y2, fill=fill_color, width=2)
