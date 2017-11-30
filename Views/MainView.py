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
        windows_xy = [(92,166),(238,164),(376,160),(87,317)]




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
            self.windows.append(Buttonslight(self,i+1, self.__arduino))
            self.windows[i].place(x= self.WindowsReferences.windows_xy[i][0] , y =self.WindowsReferences.windows_xy[i][1])


    def create_UI(self):
        self.ui_background()
        self.ui_windows()

    def show_temperature(self, int_temperature1, int_temperature2):
        self.side_view.update_temperature_text(str(int_temperature1), str(int_temperature2))


