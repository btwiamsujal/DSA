class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def is_palindrome(subs):
            return subs == subs[::-1]

        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return is_palindrome(s[i+1:j+1]) or is_palindrome(s[i:j])
            i += 1
            j -= 1
        return True
