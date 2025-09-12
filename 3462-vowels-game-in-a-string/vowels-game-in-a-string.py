class Solution(object):
    def doesAliceWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        vowels = set("aeiou")
        vowel_count = sum(ch in vowels for ch in s)
        return vowel_count > 0