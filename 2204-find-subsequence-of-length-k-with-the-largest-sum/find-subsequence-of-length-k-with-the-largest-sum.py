class Solution(object):
    def maxSubsequence(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        indexed_nums = list(enumerate(nums))
        top_k = sorted(indexed_nums, key=lambda x: x[1], reverse=True)[:k]
        top_k.sort(key=lambda x: x[0])
        return [x[1] for x in top_k]