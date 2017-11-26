from tkinter import Frame, Label, Button, N, E, W, S


class SideView(Frame):
    class Constants:
        center = N + W + S + E

    def __init__(self):
        super().__init__()

        self.__label = Label(self)

        self.__label.grid(row = 0, column = 2, sticky = self.Constants.center)

        self.grid_rowconfigure(0, weight=True)
        self.grid_columnconfigure(0, weight=True)
        self.grid_columnconfigure(0, weight=True)

        self.update_temperature_text("0")

        self.build()

    def build(self):
        pass

    def update_temperature_text(self, int_temp):
        text = str(int_temp)
        text = 'Temperature: ' + text + "º"
        self.__label.configure(text = text, font = ('Arial',12))