import serial

class ArduinoController():

    class Constants:
        port = '/dev/cu.usbmodem1421'
        baudio = 115200

    def __init__(self):
        try:
            self.__arduino = serial.Serial(self.Constants.port,self.Constants.baudio)
        except Exception:
            print("Arduino no ha conectado correctamente")

    def on_closing(self):
        self.__arduino.close()


    def send_instruction(self,instruction):
        value = str(instruction).encode('ascii')
        self.__arduino.write(value)

    def sensor_instruction(self,instruction):
        value = str(instruction).encode('ascii')
        self.__arduino.write(value)

    def read_arduino(self):
        data = self.__arduino.readline().decode()
        return data
