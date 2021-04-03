import unittest

from shuffle_the_array import Solution


class ShuffleTheArrayTest(unittest.TestCase):

    def test_four_array_elements(self):
        nums = [1, 1, 2, 2]
        n = 2
        output = [1, 2, 1, 2]

        self.assertEqual(Solution().shuffle(nums, n), output)

    def test_2npair_array(self):
        nums = [1, 2, 3, 4, 4, 3, 2, 1]
        n = 4
        output = [1, 4, 2, 3, 3, 2, 4, 1]

        self.assertEqual(Solution().shuffle(nums, n), output)

    def test_2nodd_array(self):
        nums = [2, 5, 1, 3, 4, 7]
        n = 3
        output = [2, 3, 5, 4, 1, 7]

        self.assertEqual(Solution().shuffle(nums, n), output)
