class Solution(object):
    def productQueries(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        MOD = 10**9 + 7
        
        powers = []
        bit = 0
        while n > 0:
            if n & 1:
                powers.append(1 << bit)
            n >>= 1
            bit += 1
        
        prefix = [1]
        for p in powers:
            prefix.append((prefix[-1] * p) % MOD)
        
        ans = []
        for l, r in queries:
            num = prefix[r+1]
            den = pow(prefix[l], MOD-2, MOD) 
            ans.append((num * den) % MOD)
        
        return ans
