import unittest
from expressions_matter import expression_matter


class ExpressionsMatterTest(unittest.TestCase):
    def test_small_values(self):
        self.assertEqual(expression_matter(2, 1, 2), 6)
        self.assertEqual(expression_matter(2, 1, 1), 4)
        self.assertEqual(expression_matter(1, 1, 1), 3)
        self.assertEqual(expression_matter(1, 2, 3), 9)
        self.assertEqual(expression_matter(1, 3, 1), 5)
        self.assertEqual(expression_matter(2, 2, 2), 8)

    def test_medium_values(self):
        self.assertEqual(expression_matter(5, 1, 3), 20)
        self.assertEqual(expression_matter(3, 5, 7), 105)
        self.assertEqual(expression_matter(5, 6, 1), 35)
        self.assertEqual(expression_matter(1, 6, 1), 8)
        self.assertEqual(expression_matter(2, 6, 1), 14)
        self.assertEqual(expression_matter(6, 7, 1), 48)

    def test_mixed_values(self):
        self.assertEqual(expression_matter(2, 10, 3), 60)
        self.assertEqual(expression_matter(1, 8, 3), 27)
        self.assertEqual(expression_matter(9, 7, 2), 126)
        self.assertEqual(expression_matter(1, 1, 10), 20)
        self.assertEqual(expression_matter(9, 1, 1), 18)
        self.assertEqual(expression_matter(10, 5, 6), 300)
        self.assertEqual(expression_matter(1, 10, 1), 12)


if __name__ == '__main__':
    unittest.main()
