class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) 
        if n <= 1:
            return 0
        elif n == 2:
            diff = abs(nums[0] - nums[1])
            return diff
        else:
            nums.sort()
            diff = 0
            for i in range(1, n):
                k = abs(nums[i] - nums[i-1])
                diff = max(diff, k)
            return diff


        