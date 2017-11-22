from tkinter import Label

class Buttons(Label):

    class Constants:
        on = "#FEFFE3"
        off = "black"


    class Events:
        click = "<Button-1>"
        double_click = "<Double-1>"

    def __init__(self, parent):
        super().__init__(parent)
        self.config(bg = self.Constants.off)
        self.__light_is_on = False
        self.bind(self.Events.click, self.__turn_light())

    def __turn_light(self):
        if self.__light_is_on:
            self.config(bg = self.Constants.off)
            self.__light_is_on = False
            print("funciona")
        else:
            self.config(bg=self.Constants.on)
            self.__light_is_on = True
            print("ok")

