class Solution(object):
    def maxSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        ans = set(nums)
        val = 0
        neg_nums = -100000
        flag = False
        for num in ans:
            if num > 0:
                val += num
                flag = True
            elif num <= 0:
                neg_nums = max(neg_nums, num)
            
        
        return val if flag else neg_nums