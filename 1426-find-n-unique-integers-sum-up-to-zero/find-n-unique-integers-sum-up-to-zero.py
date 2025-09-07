class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = []
        if n % 2 == 1:
            result.append(0)

        for i in range(1, n // 2 + 1):
            result.append(i)
            result.append(-i)
        
        return result