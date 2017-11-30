from tkinter import Label, PhotoImage

from Models.Commands import Commands

class Buttonslight(Label):



    class Events:
        click = "<Button-1>"
        double_click = "<Double-1>"

    def __init__(self, parent, number_room, arduino):
        super().__init__(parent)
        self.__manager_arduino = arduino
        self.img_off = PhotoImage(file = Commands.References.references[number_room-1][0])
        self.img_on = PhotoImage(file = Commands.References.references[number_room-1][1])
        self.config(image = self.img_off)
        self.number_room= number_room
        self.config(bd = 0)
        self.__light_is_on = False
        self.bind(self.Events.click, self.__turn_light)

        self.__command = Commands()

    def __turn_light(self, event):
        if self.__light_is_on:
            if self.number_room != 5:
                self.config(image=self.img_off)
                self.__light_is_on = False
                self.__manager_arduino.send_instruction(self.__command.choise_command(self.__light_is_on,self.number_room))
            else:
                self.config(image=self.img_off)
                self.__light_is_on = False
                self.__manager_arduino.send_instruction(Commands.Constants.garaje_state[0])

        else:
            if self.number_room != 5:
                self.config(image=self.img_on)
                self.__light_is_on = True
                self.__manager_arduino.send_instruction(self.__command.choise_command(self.__light_is_on, self.number_room))
            else:
                self.config(image=self.img_on)
                self.__light_is_on = True
                self.__manager_arduino.send_instruction(Commands.Constants.garaje_state[1])

    @classmethod
    def number_room(cls):
        return cls.number_room