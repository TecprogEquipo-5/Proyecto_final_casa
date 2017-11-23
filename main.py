from Views.MainView import MainView
from Models.MessageManager import MessageManager

class MainApp():
    def __init__(self):
        self.__master = MainView(send_handler = self.__send)
        self.__client = MessageManager()


    def run(self):
        self.__master.mainloop()

    def __send(self):
        self.__client.send_message()


if __name__ == "__main__":
    app = MainApp()
    app.run()