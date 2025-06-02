class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxm = float('-inf')
        s = 0
        for i in range(len(nums)):
		    s += nums[i]
		    if s > maxm:
			    maxm = s
		    if s < 0:
			    s = 0
        return maxm