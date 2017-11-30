from tkinter import Frame, Label, Button, PhotoImage,S, N, E, W

from Views.Buttonlight import Buttonslight


class SideView(Frame):
    class Constants:
        width = 298
        height = 1000
        center = N + S + E + W

    def __init__(self, parent,arduino,list_buttons):
        super().__init__(parent)
        self.__arduino = arduino
        self.configure(width = self.Constants.width, height =self.Constants.height)
        self.build()
        self.list_buttons =list_buttons

    def build(self):
        #boton todas las luces ON/OFF
        self.__button_all_lights = Buttonslight(self,5, 10,10,self.__arduino)
        self.__button_all_lights.config(text = "OFF ALL", font = "Comicsans", bg = 'brown',foreground = 'white')

        self.__button_all_lights.grid(row = 0, column = 0, sticky = self.Constants.center)

    def off_all(self):
        for i in range(0, 4):
            self.list_buttons[i].forced_off


