from Models.Commands import Commands
from Models.MessageManager import MessageManager

class SecurityController():
    class Constants:
        on_off = 4
        delay_buzz_ms = 4000

    def __init__(self, master, arduino):
        self.arduino_controller = arduino
        self.master = master
        #self.__msn_manager = MessageManager()
        self.__system_on = False
        self.alerts_active = False


    def is_move(self, data, is_system_on):
        try:
            if int(data) >= 850 and is_system_on == True :
                if self.alerts_active == False:
                    #self.arduino_controller.send_instruction(Commands.Constants.on_commands[self.Constants.on_off])
                    #self.__msn_manager.send_message()
                    print(data)
                    print("mensaje enviado")
                    self.alerts_active = True
                    self.alarm()
            else:
                self.alerts_active = False
                #self.arduino_controller.send_instruction(Commands.Constants.off_commands[self.Constants.on_off])
        except Exception:
            pass

    def alarm(self):
        self.arduino_controller.send_instruction(Commands.Constants.on_commands[self.Constants.on_off])
        self.master.after(self.Constants.delay_buzz_ms,self.off_buzzer)

    def off_buzzer(self):
        self.arduino_controller.send_instruction(Commands.Constants.off_commands[self.Constants.on_off])