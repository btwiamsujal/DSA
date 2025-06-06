class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pos = []
        neg = []
        for i in range(len(nums)):
            if nums[i] > 0:
                pos.append(nums[i])
            else:
                neg.append(nums[i])
        ans = []
        for i in range(len(nums)):
            if i % 2 == 0:
                k = pos.pop(0)
                ans.append(k)
            else:
                k = neg.pop(0)
                ans.append(k)
        return ans
                    