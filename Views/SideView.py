from tkinter import Frame, Label, Button, N, E, W, S, PhotoImage


class SideView(Frame):
    class Constants:
        width = 298
        height = 1000
        center = N + W + S + E
        font = 'Apple Chancery'
        font_size = 20



    def __init__(self, parent):
        super().__init__()
        self.configure(width=self.Constants.width, height=self.Constants.height)
        self.__label = Label(self,width =25, height=10 )

        self.build()


    def build(self):
        self.__label.place(x=20,y=0)

    def update_temperature_text(self, text_temp1, text_temp2):
        text = '·Temperatura cuarto 1: ' + text_temp1 + "º" + "\n" + '·Temperatura cuarto 2: ' + text_temp2 + "º"+ "\n" + "Sistema de seguridad"
        self.__label.configure(text = text, font = (self.Constants.font,self.Constants.font_size))

