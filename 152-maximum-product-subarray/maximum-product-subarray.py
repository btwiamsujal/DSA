class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pfx = 1 
        sfx = 1
        ans = float('-inf')
        n = len(nums)

        for i in range(n):
            if pfx == 0:
                pfx = 1
            if sfx == 0:
                sfx = 1

            pfx *= nums[i]
            sfx *= nums[n - i - 1]

            ans = max(ans, pfx, sfx, nums[i], nums[n - i - 1])
        
        return ans