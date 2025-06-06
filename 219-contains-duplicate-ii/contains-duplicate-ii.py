class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) == len(set(nums)):
            return False
        for i in range(len(nums)):
            j = i + 1
            while j < len(nums):
                if i != j and nums[i] == nums[j] and abs(i - j) <= k:
                    return True
                j += 1
        return False