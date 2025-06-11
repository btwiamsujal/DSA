class Solution(object):
    def greatestLetter(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = []
        for char in s:
            if char.islower() and char.upper() in s:
                ans.append(char.upper())
        if not ans:
            return ""   
        maxm = ord(ans[0])
        for val in ans:
            maxm = max(maxm, ord(val))
        return chr(maxm)