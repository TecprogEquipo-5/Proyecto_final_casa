from tkinter import Frame, Label, Button, PhotoImage


class SideView(Frame):
    class Constants:
        width = 298
        height = 1000

    def __init__(self, parent):
        super().__init__(parent)
        self.configure(width = self.Constants.width, height =self.Constants.height)
        self.build()

    def build(self):
        self.config(bg = "blue")
