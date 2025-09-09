class Solution(object):
    def peopleAwareOfSecret(self, n, delay, forget):
        """
        :type n: int
        :type delay: int
        :type forget: int
        :rtype: int
        """
        MOD = 10**9 + 7
        dp = [0] * (n + 1)
        
        # Day 1: one person knows the secret
        dp[1] = 1
        
        # Number of people currently sharing the secret
        sharing = 0
        
        # Total number of people who know the secret
        total_aware = 1
        
        for i in range(2, n + 1):
            # People who start sharing on day i
            # These are the people who learned the secret on day i - delay
            # We add them to our 'sharing' count.
            if i - delay >= 1:
                sharing = (sharing + dp[i - delay]) % MOD
            
            # People who forget the secret on day i
            # These are the people who learned the secret on day i - forget
            # We subtract them from both 'sharing' and 'total_aware'.
            if i - forget >= 1:
                sharing = (sharing - dp[i - forget] + MOD) % MOD
                total_aware = (total_aware - dp[i - forget] + MOD) % MOD
            
            # The number of new people who learn the secret on day i
            # is equal to the number of people currently sharing.
            dp[i] = sharing
            
            # Update the total number of people who know the secret
            total_aware = (total_aware + dp[i]) % MOD
            
        return total_aware