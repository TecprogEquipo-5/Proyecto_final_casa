
class Commands():

    class Constants:

        on_commands = ['A','B', 'C', 'D']
        off_commands = ['a','b', 'c', 'd']
        fan_on = 'F'
        fan_off = 'f'
        temp_sensor = 0
        move_sensor = 1


    @classmethod
    def choise_command(cls, state, number_room):
        if  state:
            return cls.Constants.on_commands[number_room-1]
        else:
            return cls.Constants.off_commands[number_room-1]