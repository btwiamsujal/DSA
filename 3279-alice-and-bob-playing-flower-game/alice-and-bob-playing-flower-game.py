class Solution(object):
    def flowerGame(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        odd_n = (n + 1) // 2
        even_n = n // 2

        odd_m = (m + 1) // 2
        even_m = m // 2

        
        case1_pairs = odd_n * even_m
        case2_pairs = even_n * odd_m

        return case1_pairs + case2_pairs