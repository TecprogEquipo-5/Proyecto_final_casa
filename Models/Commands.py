
class Commands():

    class Constants:

        on_commands = ['A','B', 'C', 'D','T']
        off_commands = ['a','b', 'c', 'd','t']

    @classmethod
    def choise_command(cls, state, number_room):
        if  state:
            return cls.Constants.on_commands[number_room-1]
        else:
            return cls.Constants.off_commands[number_room-1]