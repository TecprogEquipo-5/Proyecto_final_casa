class TemperatureController():
    def __init__(self):
        super().__init__()
        self.__state = 'f'


    def handle_data(self, data):
        clean_values = data.strip(' \n\r').split(",")
        return clean_values[0]

    def handle_fan(self, data):
        if int(data) > 200:
            self.__state = 'F'
        else:
            self.__state = 'f'
        return self.__state

    def handle_temperature(self, bits_temp):
        value = int(bits_temp)
        temperature = (value * 150)/1024;
        return int(temperature)