import unittest
from testing_123 import number


class TestingOneTwoThree(unittest.TestCase):
    def test_number(self):
        self.assertEqual(number([]), [])
        self.assertEqual(number(["a", "b", "c"]), ["1: a", "2: b", "3: c"])


if __name__ == "__main__":
    unittest.main()
