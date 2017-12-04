from tkinter import Label, PhotoImage
from Models.Commands import Commands
from Models.MessageManager import MessageManager

class SecurityController():
    class Constants:
        on_off = 4
        delay_buzz_ms = 4000


    class Events:
        click = "<Button-1>"

    def __init__(self, master, arduino, side_view):
        self.arduino_controller = arduino
        self.master = master
        self.side_view = side_view
        self.__msn_manager = MessageManager()
        self.__system_on = False
        self.alerts_active = False
        self.on = PhotoImage(file="Assets/on.ppm")
        self.off = PhotoImage(file="Assets/off.ppm")
        self.button_security = Label(self.side_view, width = 200, height=150)
        self.make_button()


    def is_move(self, data):
        try:
            if int(data) >= 500 and self.__system_on == True :
                if self.alerts_active == False:
                    self.arduino_controller.send_instruction(Commands.Constants.on_commands[self.Constants.on_off])
                    try:
                     self.__msn_manager.send_message()
                    except Exception:
                        pass
                    print("mensaje enviado")
                    self.alerts_active = True
                    self.alarm()
            else:
                self.alerts_active = False
                self.arduino_controller.send_instruction(Commands.Constants.off_commands[self.Constants.on_off])
        except Exception:
            pass

    def alarm(self):
        self.arduino_controller.send_instruction(Commands.Constants.on_commands[self.Constants.on_off])
        self.master.after(self.Constants.delay_buzz_ms,self.off_buzzer)

    def off_buzzer(self):
        self.arduino_controller.send_instruction(Commands.Constants.off_commands[self.Constants.on_off])

    def change_sys_status(self,event):
        if self.__system_on:
            self.__system_on = False
            self.button_security.config(image = self.off)

        else:
            self.__system_on = True
            self.button_security.config(image=self.on)


    def make_button(self):
        self.button_security.config(image = self.off)
        self.button_security.place(x=40, y = 210)
        self.button_security.bind(self.Events.click, self.change_sys_status)
