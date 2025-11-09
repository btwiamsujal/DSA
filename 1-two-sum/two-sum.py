class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        q = []
        for i in range(len(nums)):
            ans = target - nums[i]
            if ans in nums and nums.index(ans) != i:
                idx = nums.index(ans)
                q.append(i)
                q.append(idx)
                break
        return q
