from tkinter import Frame, Label, Button, N, E, W, S


class SideView(Frame):
    class Constants:
        center = N + W + S + E

    def __init__(self, parent):
        super().__init__(parent)

        self.__label = Label(self)

        self.__label.grid(row = 0, column = 2, sticky = self.Constants.center)

        self.grid_rowconfigure(0, weight=True)
        self.grid_columnconfigure(0, weight=True)
        self.grid_columnconfigure(0, weight=True)

        self.update_temperature("0")

        self.build()

    def build(self):
        pass

    def update_temperature(self, int_temp):
        pass
