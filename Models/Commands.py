
class Commands():

    class Constants:

        on_commands = ['A', 'B', 'C', 'D','Z']
        off_commands = ['a', 'b', 'c', 'd','z']
        fan_on = ['F', 'G']
        fan_off = ['f', 'g']
        temp_sensor1 = 0
        temp_sensor2 = 1
        move_sensor = 2
    class References:
        references = [("Assets/w1of.gif","Assets/w1o.gif"),("Assets/w2of.gif","Assets/w2o.gif"),("Assets/w3of.gif","Assets/w3o.gif"),("Assets/w4of.gif","Assets/w4o.gif")]

    @classmethod
    def choise_command(cls, state, number_room):
        if  state:
            return cls.Constants.on_commands[number_room-1]
        else:
            return cls.Constants.off_commands[number_room-1]