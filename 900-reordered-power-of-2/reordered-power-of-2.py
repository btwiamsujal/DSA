class Solution(object):
    def reorderedPowerOf2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        target = sorted(str(n))
        for i in range(31):  
            if sorted(str(1 << i)) == target:
                return True
        return False