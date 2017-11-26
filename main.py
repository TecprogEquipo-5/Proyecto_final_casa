from Views.MainView import MainView
from Views.SideView import SideView
from Models.ArduinoController import ArduinoController
from Models.TemperatureController import TemperatureController

class MainApp():
    def __init__(self):
        self.arduino_controller = ArduinoController()
        self.__master = MainView(self.arduino_controller)
        self.__master.protocol("WM_DELETE_WINDOW", self.closing)
        self.__temp_controller = TemperatureController()
        self.__side_view = SideView()
        self.__update_temperature()

    def __update_temperature(self):
        sensor_data = self.arduino_controller.read_arduino()
        self.bits_temperature = self.__temp_controller.handle_data(sensor_data)
        self.instruction = self.__temp_controller.handle_fan(self.bits_temperature)
        self.arduino_controller.sensor_instruction(self.instruction)

        self.int_temperature = self.__temp_controller.handle_temperature(self.bits_temperature)
        self.__side_view.update_temperature_text(str(self.int_temperature))

        self.__side_view.after(1, self.__update_temperature())

    def run(self):
        self.__master.mainloop()

    def closing(self):
        self.arduino_controller.on_closing()
        self.__master.destroy()

if __name__ == "__main__":
    app = MainApp()
    app.run()