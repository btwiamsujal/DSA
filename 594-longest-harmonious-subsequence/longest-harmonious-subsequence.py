class Solution(object):
    def findLHS(self, nums):
        nums.sort()
        ans = 0
        start = 0

        for i in range(len(nums)):
            while nums[i] - nums[start] > 1:
                start += 1
            if nums[i] - nums[start] == 1:
                ans = max(ans, i - start + 1)
        return ans
