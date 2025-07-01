class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1 or nums[0] > nums[1]:
            return 0
        if nums[len(nums)-1] > nums[len(nums)-2]:
            return len(nums)-1
        low = 1
        high = len(nums) - 2
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] > nums[mid - 1]:
                low = mid + 1
            else:
                high = mid - 1
        return -1

        # if len(nums) == 1:
        #     return 0
        # if nums[0] > nums[1]:
        #     return 0
        # if nums[len(nums)-1] > nums[len(nums)-2]:
        #     return len(nums)-1
        # for i in range(1, len(nums)-1):
        #     if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
        #         return i
        # return 0        