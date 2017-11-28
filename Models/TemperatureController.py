from Models.Commands import Commands
class TemperatureController():
    def __init__(self, arduino):
        self.arduino_controller = arduino
        self.__is_fan_on =  False;

    def handle_fan(self, data):
        if int(data) >= 200 and self.__is_fan_on == False:
            self.arduino_controller.send_instruction(Commands.Constants.fan_on)
            self.__is_fan_on = True
        elif int(data) < 200 and self.__is_fan_on == True:
            self.arduino_controller.send_instruction(Commands.Constants.fan_off)
            self.__is_fan_on = False

    def handle_temperature(self, bits_temp):
        value = int(bits_temp)
        temperature = (value * 150)/1024
        return int(temperature)