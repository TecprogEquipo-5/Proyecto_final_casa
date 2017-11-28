from tkinter import Frame, Label, Button, PhotoImage,S, N, E, W

from Views.Buttonlight import Buttonslight


class SideView(Frame):
    class Constants:
        width = 298
        height = 1000
        center = N + S + E + W

    def __init__(self, parent,arduino):
        super().__init__(parent)
        self.__arduino = arduino
        self.configure(width = self.Constants.width, height =self.Constants.height)
        self.build()

    def build(self):
        self.config(bg = "beige")

        #boton todas las luces ON/OFF
        self.__button_all_lights = Buttonslight(self,5, 20,20,self.__arduino)
        self.__button_all_lights.config(text = " ON/OFF", font = "Comicsans", bg = 'brown',foreground = 'white')

        self.__button_all_lights.grid(row = 0, column = 0, sticky = self.Constants.center)



