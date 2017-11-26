from tkinter import Tk, Label, PhotoImage, Frame
from Views.Buttonlight import Buttonslight
from Views.SideView import SideView

class MainView(Tk):
    class Constants:
        title = "Casa equipo 5"
        heigth = 500
        width = 1000
        image_dir = "Assets/casa1.gif"

    class WindowsReferences:
        windows_xy = [(106,174),(252,175),(391,172),(104,326)]
        windows_dimentions = [(5,8),(3,3),(5,13),(5,7)]




    @classmethod
    def size(cls):
        return "{}x{}".format(cls.Constants.width, cls.Constants.heigth)

    @classmethod
    def heigth_size(cls):
        return cls.Constants.heigth

    @classmethod
    def width_size(cls):
        return cls.Constants.width

    def __init__(self, arduino_controller):
        super().__init__()
        self.__arduino = arduino_controller
        self.title(self.Constants.title)
        self.geometry(self.size())
        self.minsize(self.width_size(), self.heigth_size())
        self.maxsize(self.width_size(), self.heigth_size())
        self.create_UI()
        self.side_view = SideView(self)
        self.side_view.place(x=702, y=2)
        self.side_view.tkraise()

    def ui_background(self):
        try:
            self.image_house = PhotoImage(file = self.Constants.image_dir)
            self.__back_ground = Label(self,image= self.image_house ).place(x=0, y=0).pack()
        except Exception:
            pass

        self.side_view = Frame(self,bg="black")

    def ui_windows(self):
        self.windows = []
        for i in range (0,4):
            self.windows.append(Buttonslight(self,i+1,self.WindowsReferences.windows_dimentions[i][0],self.WindowsReferences.windows_dimentions[i][1], self.__arduino))
            self.windows[i].place(x= self.WindowsReferences.windows_xy[i][0] , y =self.WindowsReferences.windows_xy[i][1])




    def create_UI(self):
        self.ui_background()
        self.ui_windows()





        


