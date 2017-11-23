from tkinter import Tk, Label, PhotoImage
from Views.Button import Buttons


class MainView(Tk):
    class Constants:
        title = "Casa equipo 5"
        heigth = 500
        width = 1000
        image_dir = "Assets/casa1.gif"

    @classmethod
    def size(cls):
        return "{}x{}".format(cls.Constants.width, cls.Constants.heigth)

    @classmethod
    def heigth_size(cls):
        return cls.Constants.heigth

    @classmethod
    def width_size(cls):
        return cls.Constants.width

    def __init__(self):
        super().__init__()
        self.title(self.Constants.title)
        self.geometry(self.size())
        self.minsize(self.width_size(), self.heigth_size())
        self.maxsize(self.width_size(), self.heigth_size())
        self.create_UI()


    def ui_background(self):
        try:
            self.image_house = PhotoImage(file = self.Constants.image_dir)
            self.__back_ground = Label(self,image= self.image_house ).place(x=0, y=0).pack()
        except Exception:
            pass

    def ui_windows(self):
        self.window1 = Buttons(self)
        self.window1.config(height = 5, width = 8)
        self.window1.place(x=105, y =175)


    def create_UI(self):
        self.ui_background()
        self.ui_windows()




        


