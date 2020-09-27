import unittest
from alphabet_position import alphabet_position
from random import randint


class TestAlphabetPosition(unittest.TestCase):
    def test_assert_type(self):
        text = "The sunset sets at twelve o' clock."
        result = alphabet_position(text)
        self.assertEqual(type(result), str)

    def test_assert_not_in_alphabet(self):
        number_test = ""
        for item in range(10):
            number_test += str(randint(1, 9))
        self.assertEqual(alphabet_position(number_test), "")
        self.assertEqual(alphabet_position("."), "")

    def test_assert_examples(self):
        self.assertEqual(alphabet_position("The narwhal bacons at midnight."),
                         "20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20")
        self.assertEqual(alphabet_position(
            "The sunset sets at twelve o' clock."), "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11")


if __name__ == '__main__':
    unittest.main()
