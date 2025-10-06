class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 2

    # Step 1: Find first decreasing element from the right
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

    # Step 2: If such element exists
        if i >= 0:
            j = n - 1
        # Find element just larger than nums[i]
            while nums[j] <= nums[i]:
                j -= 1
        # Step 3: Swap
            nums[i], nums[j] = nums[j], nums[i]

    # Step 4: Reverse the suffix
        nums[i + 1:] = reversed(nums[i + 1:])