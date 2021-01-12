import unittest
from grasshopper_summation import summation


class SummationTest(unittest.TestCase):
    def test_summ_1(self):
        self.assertEqual(summation(1), 1)

    def test_summ_8(self):
        self.assertEqual(summation(8), 36)

    def test_summ_22(self):
        self.assertEqual(summation(22), 253)

    def test_summ_100(self):
        self.assertEqual(summation(100), 5050)

    def test_summ_213(self):
        self.assertEqual(summation(213), 22791)


if __name__ == "__main__":
    unittest.main()
