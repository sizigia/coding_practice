class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return [sum(nums[:i]) for i in range(1, len(nums) + 1)]
