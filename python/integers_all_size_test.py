import unittest
from unittest.mock import MagicMock
from integers_all_size import a, b, c, d


class TestIntegers(unittest.TestCase):
    def setUp(self):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

        print("\nSETUP VARIABLES")
        return super().setUp()

    def test_ints_great(self):
        for _ in [self.a, self.b, self.c, self.d]:
            self.assertGreaterEqual(_, 1)
        print("TESTING CONSTRAINT - NUMBERS GREATER THAN OR EQUAL TO 1")

    def test_ints_less(self):
        for _ in [self.a, self.b, self.c, self.d]:
            self.assertLessEqual(_, 1000)
        print("TESTING CONSTRAINT - NUMBERS LESS THAN OR EQUAL TO 1000")

    def test_calc(self):
        self.a = 9
        self.b = 29
        self.c = 7
        self.d = 27

        res = self.a ** self.b + self.c ** self.d

        self.assertEqual(res,
                         4710194409608608369201743232)


if __name__ == '__main__':
    unittest.main()
