class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        s = sum(nums[:k])
        avg = s / float(k)
        for i in range(1, len(nums) -k  +1):
            s = s - nums[i - 1] + nums[i + k - 1]
            avg = max(avg, s / float(k))
        return avg 



        