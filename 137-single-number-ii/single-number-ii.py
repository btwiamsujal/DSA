class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        once = 0
        twos = 0
        for num in nums:
            once = (once ^ num) & ~twos
            twos = (twos ^ num) & ~once
        return once