import unittest
from find_the_parity_outlier import find_outlier


class FindOutlierTest(unittest.TestCase):
    def test_cases(self):
        self.assertEquals(find_outlier([2, 4, 6, 8, 10, 3]), 3)
        self.assertEquals(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]), 11)
        self.assertEquals(find_outlier([160, 3, 1719, 19, 11, 13, -21]), 160)


if __name__ == '__main__':
    unittest.main()
