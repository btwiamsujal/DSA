class Solution(object):
    def maxFreqSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq = {}
        for char in s:
            if char not in freq:
                freq[char] = 1
            else:
                freq[char] += 1
            
        vowel = ['a', 'e', 'i', 'o', 'u']
        f1 = 0
        f2 = 0

        for char, cnt in freq.items():
            if char in vowel:
                f1 = max(f1, cnt)       
            else:
                f2= max(f2, cnt)
            
        return f1 + f2