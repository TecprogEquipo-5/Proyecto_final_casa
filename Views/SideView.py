from tkinter import Frame, Label, Button, N, E, W, S, PhotoImage


class SideView(Frame):
    class Constants:
        width = 298
        height = 1000
        center = N + W + S + E

    def __init__(self, parent):
        super().__init__(parent)
        self.configure(width=self.Constants.width, height=self.Constants.height)
        self.build()

        self.__label = Label(self)
        self.__label.grid(row = 0, column = 1, sticky = self.Constants.center)

        self.grid_rowconfigure(0, weight=True)
        self.grid_columnconfigure(0, weight=True)
        self.grid_columnconfigure(0, weight=True)

    def build(self):
        self.config(bg="blue")

    def update_temperature_text(self, text_temp1, text_temp2):
        text = 'Temperature 1: ' + text_temp1 + "º" + "\n" + 'Temperature 2: ' + text_temp2 + "º"
        self.__label.configure(text = text, font = ('Arial',12))
