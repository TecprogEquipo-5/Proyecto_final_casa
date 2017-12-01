import unittest
from Models.TemperatureController import TemperatureController

class TestTemperature(unittest.TestCase):

    def setUp(self):
        print(self._testMethodDoc)

    def test_handle_fan(self):
        """-- Test Correct Close"""
        msg = "ERROR, The program close incorrect "
        self.assertEqual(TemperatureController.handle_fan(self, int, int),None, msg = msg)

