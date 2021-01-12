import sys
import unittest
from unittest.mock import Mock, patch
from io import StringIO
from contextlib import redirect_stdout
from triangle_quest import triangle_quest_print


class TestTriangleQuest(unittest.TestCase):

    def test_input(self, input):
        with patch('builtins.input', return_value=5) as input_:
            self.assertEqual(input_, triangle_quest_print())

    def test_capture(self):
        mock_output = Mock(side_effect=['1', '22', '333', '4444'])

        self.assertEqual("1", mock_output())
        self.assertEqual("22", mock_output())
        self.assertEqual("333", mock_output())
        self.assertEqual("4444", mock_output())


if __name__ == '__main__':
    unittest.main()
