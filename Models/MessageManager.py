from twilio.rest import Client
from Models.JsonManager import JsonManager


class MessageManager():

    class Constants:
        json_dir = "Assets/twilio_information"

    def __init__(self):
        message_variables = JsonManager.open_json_file(self.Constants.json_dir)
        if message_variables is None:
            return

        account_sid = message_variables.get("account_sid", None)
        auth_token = message_variables.get("auth_token", None)
        self.__twilio_phone = message_variables.get("twilio_phone", None)
        self.message = message_variables.get("message", None)
        self.phone = message_variables.get("phone", None)
        self.__client = Client(account_sid, auth_token)

    def send_message(self):
        self.__client.messages.create( to=self.phone, from_= self.__twilio_phone, body=self.message)
        print("mensaje enviado")
