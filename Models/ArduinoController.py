import serial

class ArduinoController():

    class Constants:
        port = 'COM8'
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