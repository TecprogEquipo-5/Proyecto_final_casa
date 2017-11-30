from Views.MainView import MainView
from Models.SecurityController import SecurityController

from Models.ArduinoController import ArduinoController
from Models.TemperatureController import TemperatureController
from Models.Commands import Commands

class MainApp():
    class Constants:
        protocolo_off = "WM_DELETE_WINDOW"

    def __init__(self):
        self.ready_to_start = True

        for port in Commands.Constants.ports:
            try:
                self.arduino_controller = ArduinoController(port)
                self.ready_to_start = True
                break
            except Exception:
                self.ready_to_start = False
        if self.ready_to_start == False:
            return

        self.__master = MainView(self.arduino_controller)
        self.__master.protocol(self.Constants.protocolo_off, self.closing)
        self.__temp_controller = TemperatureController( self.arduino_controller)
        #crea la variable de SecurityController
        self.__security_controller = SecurityController(self.__master,self.arduino_controller)
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
            self.__security(sensor_data)
        self.__master.after(1, self.__update_temperature)


    def __security(self,sensor_data):
        self.bits_move_sensor = self.arduino_controller.handle_data(sensor_data,Commands.Constants.move_sensor)
        if self.bits_move_sensor != None:
            self.__security_controller.is_move(self.bits_move_sensor, True)

    def run(self):

        if self.ready_to_start != False:

           self.__master.mainloop()
        else:
            print("CONECTA EL ARDUINO PLEASE")


    def closing(self):
        try:
            self.arduino_controller.on_closing()
        except Exception:
            pass
        self.__master.destroy()

if __name__ == "__main__":
    app = MainApp()
    app.run()