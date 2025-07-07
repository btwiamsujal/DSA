class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        ans = 1
        while 4 ** ans <= n:
            if 4 ** ans == n:
                return True
            ans += 1
        return False