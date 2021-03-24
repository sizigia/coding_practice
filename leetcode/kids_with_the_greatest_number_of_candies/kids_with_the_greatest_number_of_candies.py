class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """

        greatest_n = max(candies)
        return [(kid_candies + extraCandies) >= greatest_n for kid_candies in candies]
