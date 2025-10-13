from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dq = deque()  # stores indices of potential max elements
        res = []

        for i in range(len(nums)):
            # 1. Remove elements that are out of this window
            if dq and dq[0] == i - k:
                dq.popleft()

            # 2. Remove all smaller elements (they are useless)
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            # 3. Add current element's index
            dq.append(i)

            # 4. Append max to result (once we have the first full window)
            if i >= k - 1:
                res.append(nums[dq[0]])

        return res
