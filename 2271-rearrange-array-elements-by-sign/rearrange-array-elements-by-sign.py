class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [0] * len(nums)
        pos = 0
        neg = 1
        for i in range(len(nums)):
            if nums[i] < 0:
                ans[neg] = nums[i]
                neg += 2
            else:
                ans[pos] = nums[i]
                pos += 2
        return ans
                    