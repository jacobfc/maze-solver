from cell import Cell
from time import sleep


class Maze:
    def __init__(
        self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win, sleep_timer=0.1
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.sleep_timer = sleep_timer

        # empty list of cells; populate with self.__create_cells()
        self.__cells = []
        self.__create_cells()

    def __create_cells(self):
        for column in range(self.num_cols):
            column_list = []
            for row in range(self.num_rows):
                column_list.append(Cell(self.win))

            # add each column to self.__cells
            self.__cells.append(column_list)

        # after creating cells, draw all of them
        for i in range(len(self.__cells)):
            for j in range(len(self.__cells[i])):
                self.__draw_cell(i, j)

    def __draw_cell(self, i, j):
        # i == column number, j == row number
        cell = self.__cells[i][j]

        x1 = (i * self.cell_size_x) + self.x1
        x2 = ((i + 1) * self.cell_size_x) + self.x1
        y1 = (j * self.cell_size_y) + self.y1
        y2 = ((j + 1) * self.cell_size_y) + self.y1

        cell.draw(x1, x2, y1, y2)
        self.__animate()

    def __animate(self):
        self.win.redraw()
        sleep(self.sleep_timer)
