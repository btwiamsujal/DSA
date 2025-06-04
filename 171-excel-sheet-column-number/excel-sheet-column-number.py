class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        res = 0
        for ch in columnTitle:
            val = ord(ch) - ord('A') + 1
            res = res * 26 + val

        return res