import unittest
from josephus_perm import josephus


class TestSumIntervals(unittest.TestCase):
    def test_examples(self):
        #self.assertEqual(josephus([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        #self.assertEqual(josephus([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2), [2, 4, 6, 8, 10, 3, 7, 1, 9, 5])
        self.assertEqual(josephus(["C", "o", "d", "e", "W", "a", "r", "s"], 4), [
            'e', 's', 'W', 'o', 'C', 'd', 'r', 'a'])
        self.assertEqual(josephus([1, 2, 3, 4, 5, 6, 7], 3), [
                         3, 6, 2, 7, 5, 1, 4])
        self.assertEqual(josephus([], 3), [])


if __name__ == "__main__":
    unittest.main()
