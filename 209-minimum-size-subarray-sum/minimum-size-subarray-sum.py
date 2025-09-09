class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        if sum(nums) < target:
            return 0
        if target in nums:
            return 1
        n = len(nums)
        left = 0
        total = 0
        min_len = float("inf")
        
        for right in range(n):
            total += nums[right]
            
            while total >= target:
                min_len = min(min_len, right - left + 1)
                total -= nums[left]
                left += 1
        
        return 0 if min_len == float("inf") else min_len