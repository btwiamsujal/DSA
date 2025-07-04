class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        val = 1
        i = 0
        while val <= n:
            val = 2 ** i
            if val == n:
                return True
            else:
                i += 1
        return False
