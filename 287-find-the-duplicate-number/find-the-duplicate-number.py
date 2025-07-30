class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set()
        for val in nums:
            if val in s:
                return val
            s.add(val)
        return 0

        