class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        if nums[0] != nums[1]:
            return nums[0]
        if nums[len(nums) - 1] != nums[len(nums) - 2]:
            return nums[len(nums) - 1]
        for i in range(1, len(nums) - 2):
            if nums[i - 1] != nums[i] and nums[i] != nums[i + 1]:
                return nums[i]