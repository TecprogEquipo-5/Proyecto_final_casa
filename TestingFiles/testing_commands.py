import unittest
from Models.Commands import Commands

class TestCommands(unittest.TestCase):

    def setUp(self):
        print(self._testMethodDoc)

    def test_choise_command_on(self):
        """-- Test Correct Command"""
        msg = "The command ON is not the expect "
        self.assertEqual(Commands.choise_command(True,1),'A', msg=msg)
        self.assertEqual(Commands.choise_command(True, 2), 'B', msg=msg)
        self.assertEqual(Commands.choise_command(True, 3), 'C', msg=msg)
        self.assertEqual(Commands.choise_command(True, 4), 'D', msg=msg)
        self.assertEqual(Commands.choise_command(True, 5), 'Z', msg=msg)

    def test_choise_command_off(self):
        """-- Test Correct Command"""
        msg = "The command OFF is not the expect "
        self.assertEqual(Commands.choise_command(False,1),'a', msg=msg)
        self.assertEqual(Commands.choise_command(False, 2), 'b', msg=msg)
        self.assertEqual(Commands.choise_command(False, 3), 'c', msg=msg)
        self.assertEqual(Commands.choise_command(False, 4), 'd', msg=msg)
        self.assertEqual(Commands.choise_command(False, 5), 'z', msg=msg)





