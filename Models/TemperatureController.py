from Models.Commands import Commands
class TemperatureController():
    def __init__(self, arduino):
        self.arduino_controller = arduino
        self.__status_fans = [False, False]


    def handle_fan(self, data, sensor):
        try:
            if int(data) >= 200 and self.__status_fans[sensor] == False:
                self.arduino_controller.send_instruction(Commands.Constants.fan_on[sensor])
                self.__status_fans[sensor] = True
            elif int(data) < 200 and self.__status_fans[sensor] == True:
                self.arduino_controller.send_instruction(Commands.Constants.fan_off[sensor])
                self.__status_fans[sensor] = False
        except Exception:
            pass


    def handle_temperature(self, bits_temp):
        value = int(bits_temp)
        temperature = (value * 150)/1024;
        return int(temperature)