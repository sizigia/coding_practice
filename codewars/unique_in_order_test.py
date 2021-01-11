import unittest
from unique_in_order import unique_in_order


class UniqueInOrder(unittest.TestCase):
    def test_number(self):
        self.assertEqual(unique_in_order('AAAABBBCCDAABBB'),
                         ['A', 'B', 'C', 'D', 'A', 'B'])
        self.assertEqual(unique_in_order('ABBCcAD'), [
                         'A', 'B', 'C', 'c', 'A', 'D'])
        self.assertEqual(unique_in_order([1, 2, 2, 3, 3]), [1, 2, 3])


if __name__ == "__main__":
    unittest.main()
