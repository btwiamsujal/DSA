class Solution(object):
    def numberOfWays(self, n, x):
        """
        :type n: int
        :type x: int
        :rtype: int
        """
        mod = 10**9 + 7
        powers = []
        i = 1
        while i ** x <= n:
            powers.append(i ** x)
            i += 1

        dp = [0] * (n + 1)
        dp[0] = 1

        for p in powers:
            for s in range(n, p - 1, -1):
                dp[s] = (dp[s] + dp[s - p]) % mod

        return dp[n]