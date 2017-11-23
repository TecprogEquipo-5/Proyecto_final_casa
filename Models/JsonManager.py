import json


class JsonManager():

    @staticmethod
    def open_json_file(json_name):
        try:
            infile = open(json_name + ".json",'r+')
            data = json.load(infile)
        except Exception:
            print("Archivo no encontrado, no sera posible enviar mensajes")
            return None
        return data