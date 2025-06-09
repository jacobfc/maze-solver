from cell import Cell
from time import sleep
import random


class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None,
        sleep_timer=0.1,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.sleep_timer = sleep_timer

        # check if random seed or pre-selected
        if seed is not None:
            random.seed(seed)

        # empty list of cells; populate with self.__create_cells()
        self.__cells = []
        self.__create_cells()

        # generate maze
        self.__break_entrance_and_exit()
        self.__break_walls_r(0, 0)

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
        if self.win is not None:
            self.win.redraw()
            sleep(self.sleep_timer)

    def __break_entrance_and_exit(self):
        # entrance == top-left cell in maze
        entrance_cell = self.__cells[0][0]
        entrance_cell.has_top_wall = False
        self.__draw_cell(0, 0)

        # exit == bottom-left cell in maze
        exit_cell = self.__cells[self.num_cols - 1][self.num_rows - 1]
        exit_cell.has_bottom_wall = False
        self.__draw_cell(self.num_cols - 1, self.num_rows - 1)

    def __get_adjacent_cells(self, i, j):
        # return valid adjacent cells, given that no looping is allowed in any dimension

        adjacent_cells = []
        # cell to the right:
        if (i + 1) < self.num_cols:
            adjacent_cells.append((i + 1, j))

        # cell to the left:
        if (i - 1) >= 0:
            adjacent_cells.append((i - 1, j))

        # cell below:
        if (j + 1) < self.num_rows:
            adjacent_cells.append((i, j + 1))

        # cell above
        if (j - 1) >= 0:
            adjacent_cells.append((i, j - 1))

        print(f"Cell: {i},{j} has following neighbors: \n{adjacent_cells}")
        return adjacent_cells

    def __break_walls_2_cells(self, i1, j1, i2, j2):
        cell_1 = self.__cells[i1][j1]
        cell_2 = self.__cells[i2][j2]

        if i1 > i2:  # cell_1 right of cell_2
            cell_1.has_left_wall = False
            cell_2.has_right_wall = False

        if i1 < i2:  # cell_1 left of cell_2
            cell_1.has_right_wall = False
            cell_2.has_left_wall = False

        if j1 > j2:  # cell_1 below cell_2
            cell_1.has_top_wall = False
            cell_2.has_bottom_wall = False

        if j1 < j2:  # cell_1 above cell_2
            cell_1.has_bottom_wall = False
            cell_2.has_top_wall = False

        # draw both cells after breaking wall
        self.__draw_cell(i1, j1)
        self.__draw_cell(i2, j2)

    def __break_walls_r(self, i, j):
        # 1) Mark the current cell as visited
        self.__cells[i][j].visited_during_generation = True

        # 2) In an infinite loop:
        while True:
            print(f"\nCurrent cell: {i},{j}")
            # a) Create a new empty list to hold the i and j values you will need to visit
            cells_to_possibly_visit = []

            # b) Check the cells that are directly adjacent to the current cell.
            # Keep track of any that have not been visited as "possible directions" to move to
            adjacent_cells = self.__get_adjacent_cells(i, j)
            for tuple in adjacent_cells:
                x, y = tuple
                if self.__cells[x][y].visited_during_generation is False:
                    cells_to_possibly_visit.append(tuple)

            print(
                f"Number of neighbors to possibly visit: {len(cells_to_possibly_visit)}"
            )
            print(f"There neighbors are: {cells_to_possibly_visit}")

            # c) If there are zero directions you can go from the current cell,
            # then draw the current cell and return to break out of the loop
            if len(cells_to_possibly_visit) == 0:
                self.__draw_cell(i, j)
                return

            # d) Otherwise, pick a random direction
            random_direction = random.randrange(len(cells_to_possibly_visit))
            random_direction_i = cells_to_possibly_visit[random_direction][0]
            random_direction_j = cells_to_possibly_visit[random_direction][1]

            # e) Knock down the walls between the current cell and the chosen cell.
            self.__break_walls_2_cells(i, j, random_direction_i, random_direction_j)

            # f) Move to the chosen cell by recursively calling _break_walls_r
            self.__break_walls_r(random_direction_i, random_direction_j)
