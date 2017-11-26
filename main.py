from Views.MainView import MainView
from Models.ArduinoController import ArduinoController

class MainApp():
    def __init__(self):
        self.arduino_controller = ArduinoController()
        self.__master = MainView(self.arduino_controller)
        self.__master.protocol("WM_DELETE_WINDOW", self.closing)

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