class Solution(object):
    def countHillValley(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cleaned = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                cleaned.append(nums[i])
        count = 0
        for i in range(1, len(cleaned) - 1):
            if cleaned[i] > cleaned[i - 1] and cleaned[i] > cleaned[i + 1]:
                count += 1
            elif cleaned[i] < cleaned[i - 1] and cleaned[i] < cleaned[i + 1]:
                count += 1
        return count
        