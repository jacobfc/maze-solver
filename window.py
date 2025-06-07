from tkinter import Tk, Canvas  # ,BOTH


class Window:
    def __init__(self, width, height):
        self.__root_widget = Tk()
        self.__root_widget.title("Maze Solver")

        self.__canvas_widget = Canvas()
        self.__canvas_widget.pack()

        self.__window_is_running = False
        self.__root_widget.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root_widget.update_idletasks()
        self.__root_widget.update()

        # TODO: unsure if this is necessary, or if doing it on the root widget is enough?
        self.__canvas_widget.update_idletasks()
        self.__canvas_widget.update()

    def wait_for_close(self):
        self.__window_is_running = True
        while self.__window_is_running:
            self.redraw()

    def close(self):
        self.__window_is_running = False

    def draw_line(self, line, fill_color):
        line.draw(self.__canvas_widget, fill_color)
