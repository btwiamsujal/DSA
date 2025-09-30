class Solution(object):
    def triangularSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        while len(nums) > 1:
            nums = [(nums[i] + nums[i+1]) % 10 for i in range(len(nums)-1)]
        return nums[0]