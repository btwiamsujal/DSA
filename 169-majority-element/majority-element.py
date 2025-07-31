class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = 0
        for i in range(len(nums)):
            if cnt == 0:
                cnt = 1
                el = nums[i]
            elif nums[i] == el:
                cnt += 1
            else:
                cnt -= 1
            
        k = nums.count(el)
        if k > len(nums) // 2:
            return el
        return -1