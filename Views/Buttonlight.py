from tkinter import Label

class Buttonslight(Label):

    class Constants:
        on = "#FEFFE3"
        off = "black"


    class Events:
        click = "<Button-1>"
        double_click = "<Double-1>"

    def __init__(self, parent, number_room,height,width, arduino):
        super().__init__(parent)
        self.config(bg = self.Constants.off)
        self.config(height = height, width =width)
        self.number_room= number_room
        self.__light_is_on = False
        self.bind(self.Events.click, self.__turn_light)

    def __turn_light(self, event):
        if self.__light_is_on:
            self.config(bg = self.Constants.off)
            self.__light_is_on = False
            print(self.number_room)
        else:
            self.config(bg=self.Constants.on)
            self.__light_is_on = True
            print("ok")


    @classmethod
    def number_room(cls):
        return cls.number_room