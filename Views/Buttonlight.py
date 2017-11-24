from tkinter import Label

from Models.Commands import Commands

class Buttonslight(Label):

    class Constants:
        on = "#FEFFE3"
        off = "black"


    class Events:
        click = "<Button-1>"
        double_click = "<Double-1>"

    def __init__(self, parent, number_room,height,width, arduino):
        super().__init__(parent)
        self.__manager_arduino = arduino
        self.config(bg = self.Constants.off)
        self.config(height = height, width =width)
        self.number_room= number_room
        self.__light_is_on = False
        self.bind(self.Events.click, self.__turn_light)

        self.__command = Commands()

    def __turn_light(self, event):
        if self.__light_is_on:
            self.config(bg = self.Constants.off)
            self.__light_is_on = False
            self.__manager_arduino.send_instruction(self.__command.choise_command(self.__light_is_on,self.number_room))
        else:
            self.config(bg=self.Constants.on)
            self.__light_is_on = True
            self.__manager_arduino.send_instruction(self.__command.choise_command(self.__light_is_on, self.number_room))


    @classmethod
    def number_room(cls):
        return cls.number_room