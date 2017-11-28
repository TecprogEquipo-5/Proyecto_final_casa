from Views.MainView import MainView

from Models.ArduinoController import ArduinoController
from Models.TemperatureController import TemperatureController
from Models.Commands import Commands

class MainApp():
    def __init__(self):
        self.arduino_controller = ArduinoController()
        self.__master = MainView(self.arduino_controller)
        self.__master.protocol("WM_DELETE_WINDOW", self.closing)
        self.__temp_controller = TemperatureController(self.arduino_controller)
        self.__update_temperature()


    def __update_temperature(self):
        sensor_data = self.arduino_controller.read_arduino()

        self.bits_temperature_sensor1 = self.arduino_controller.handle_data(sensor_data, Commands.Constants.temp_sensor1)
        self.bits_temperature_sensor2 = self.arduino_controller.handle_data(sensor_data, Commands.Constants.temp_sensor2)

        if self.bits_temperature_sensor1 != None or self.bits_temperature_sensor2 != None:

            self.__temp_controller.handle_fan(self.bits_temperature_sensor1, Commands.Constants.temp_sensor1)
            self.__temp_controller.handle_fan(self.bits_temperature_sensor2, Commands.Constants.temp_sensor2)

            self.int_temperature1 = self.__temp_controller.handle_temperature(self.bits_temperature_sensor1)
            self.int_temperature2 = self.__temp_controller.handle_temperature(self.bits_temperature_sensor2)

            self.__master.show_temperature(self.int_temperature1, self.int_temperature2)


        self.__master.after(1, self.__update_temperature)


    def run(self):
        self.__master.mainloop()

    def closing(self):
        try:
            self.arduino_controller.on_closing()
        except Exception:
            pass
        self.__master.destroy()

if __name__ == "__main__":
    app = MainApp()
    app.run()