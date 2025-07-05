class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        f = {}
        for num in arr:
            if num in f:
                f[num] += 1
            else:
                f[num] = 1
        m = -1
        for n, q in f.items():
            if n == q:
                m = max(m, n)
        return m
