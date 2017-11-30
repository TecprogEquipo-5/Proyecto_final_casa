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
        self.__review_button()
        self.__command = Commands()
        self.my_container = parent

    def __turn_light(self, event):
        if self.__light_is_on:
            self.config(bg = self.Constants.off)
            self.__light_is_on = False
            self.__manager_arduino.send_instruction(self.__command.choise_command(self.__light_is_on,self.number_room))
        else:
            self.config(bg=self.Constants.on)
            self.__light_is_on = True
            self.__manager_arduino.send_instruction(self.__command.choise_command(self.__light_is_on, self.number_room))

    def __off_all_lights(self,event):
        self.__manager_arduino.send_instruction(self.__command.choise_command(self.__light_is_on, self.number_room))
        self.my_container.off_all()

    def __review_button(self):
        if self.number_room == 5:
            self.bind(self.Events.click, self.__off_all_lights)
        else:
            self.bind(self.Events.click, self.__turn_light)


    def forced_off(self):
        self.__light_is_on = False
        self.config(bg = 'black')


    @classmethod
    def number_room(cls):
        return cls.number_room




