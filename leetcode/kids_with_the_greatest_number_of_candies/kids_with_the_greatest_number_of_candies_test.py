import unittest

from kids_with_the_greatest_number_of_candies import Solution


class KidsWithCandiesTest(unittest.TestCase):

    def test_one_kid_greatest_no_candies(self):
        candies = [4, 2, 1, 1, 2]
        extraCandies = 1
        expected_output = [True, False, False, False, False]

        self.assertEqual(Solution().kidsWithCandies(
            candies, extraCandies), expected_output)

    def test_two_kids_greatest_no_candies(self):
        candies = [12, 1, 12]
        extraCandies = 10
        expected_output = [True, False, True]

        self.assertEqual(Solution().kidsWithCandies(
            candies, extraCandies), expected_output)

    def test_several_kids_greatest_no_candies(self):
        candies = [2, 3, 5, 1, 3]
        extraCandies = 3
        expected_output = [True, True, True, False, True]

        self.assertEqual(Solution().kidsWithCandies(
            candies, extraCandies), expected_output)


if __name__ == '__main__':
    unittest.main()
