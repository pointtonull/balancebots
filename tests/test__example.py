import unittest

from lib.matrix import Matrix
import time


INSTRUCTIONS = [
        "value 5 goes to bot 2",
        "bot 2 gives low to bot 1 and high to bot 0",
        "value 3 goes to bot 1",
        "bot 1 gives low to output 1 and high to bot 0",
        "bot 0 gives low to output 2 and high to output 0",
        "value 2 goes to bot 2",
    ]

TARGET = set([5, 2])
RESULT = "bot 2"


class TestExample(unittest.TestCase):
    """
    Tests the given example
    """

    def setUp(self):
        self.matrix = Matrix(TARGET)

    def test__result_is_right(self):
        for instruction in INSTRUCTIONS:
            self.matrix.execute_instruction(instruction)
        self.matrix.done.wait()
        time.sleep(.1)
        self.assertEqual(RESULT, str(self.matrix.result))

