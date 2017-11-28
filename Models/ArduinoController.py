import serial

class ArduinoController():

    class Constants:
        port = '/dev/cu.usbmodem1411'
        baudio = 115200

    def __init__(self):
        self.__arduino = serial.Serial(self.Constants.port,self.Constants.baudio)

    def on_closing(self):
        self.__arduino.close()

    def send_instruction(self,instruction):
        value = str(instruction).encode('ascii')
        self.__arduino.write(value)

    def handle_data(self, data, sensor_type):
        try:
            clean_values = data.strip(' \n\r').split(",")
            return clean_values[sensor_type]
        except Exception:
            pass

    def read_arduino(self):
        try:
            data = self.__arduino.readline().decode()
            return data
        except Exception:
            pass