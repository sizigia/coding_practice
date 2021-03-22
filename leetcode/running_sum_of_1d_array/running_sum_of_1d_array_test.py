import unittest
from running_sum_of_1d_array import Solution


class RunningSum(unittest.TestCase):

    def test_simple_list(self):
        self.assertEqual(Solution().runningSum([1, 2, 3, 4]), [1, 3, 6, 10])

    def test_list_with_identical_elements(self):
        self.assertEqual(Solution().runningSum(
            [1, 1, 1, 1, 1]), [1, 2, 3, 4, 5])

    def test_list_with_unordered_elements(self):
        self.assertEqual(
            Solution().runningSum([3, 1, 2, 10, 1]),
            [3, 4, 6, 16, 17]
        )


if __name__ == '__main__':
    unittest.main()
