import sys
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 0
        high = len(nums) - 1
        ans = sys.maxsize
        if nums[low] <= nums[high]:
            return nums[low]
        while (low <= high):
            mid = (low + high) // 2
            ans = min(ans, nums[mid])
            if nums[low] <= nums[mid]:
                ans = min(ans, nums[low])
                low = mid + 1
            else:
                high = mid - 1

        return ans
                
