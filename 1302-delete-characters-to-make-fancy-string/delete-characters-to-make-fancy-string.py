class Solution(object):
    def makeFancyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return None
        if len(s) == 1:
            return str(s)
        ans = ""
        ans += s[0]
        ans += s[1]
        for i in range(2, len(s)):
            if s[i-2] == s[i-1] == s[i]:
                continue
            ans += s[i]
        return ans