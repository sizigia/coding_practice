import unittest
from convert_fracs import convertFracts


class TestLCM(unittest.TestCase):
    def test_examples(self):
        a = [[1, 2], [1, 3], [1, 4]]
        b = [[6, 12], [4, 12], [3, 12]]
        self.assertEqual(convertFracts(a), b)

        a = []
        b = []
        self.assertEqual(convertFracts(a), b)


if __name__ == "__main__":
    unittest.main()
