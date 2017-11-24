from tkinter import Frame, Label, Button


class SideView(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(width = 400, height =300)
        self.build()

    def build(self):
        self.configure(bg = "blue")
        self.side_label = Label(self, background= "black", width =100, height = 200)
        self.side_label.place(x=0, y=0)


