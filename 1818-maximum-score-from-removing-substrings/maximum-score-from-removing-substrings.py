class Solution(object):
    def maximumGain(self, s, x, y):
        """
        :type s: str
        :type x: int
        :type y: int
        :rtype: int
        """
        s2 = s[:]  
        ans = 0

        if x > y:
            i = 0
            while i < len(s2) - 1:
                if s2[i] == 'a' and s2[i+1] == 'b':
                    s2 = s2[:i] + s2[i+2:]
                    ans += x
                    i = max(i - 1, 0)
                else:
                    i += 1

            i = 0
            while i < len(s2) - 1:
                if s2[i] == 'b' and s2[i+1] == 'a':
                    s2 = s2[:i] + s2[i+2:]
                    ans += y
                    i = max(i - 1, 0)
                else:
                    i += 1

        else:
            i = 0
            while i < len(s2) - 1:
                if s2[i] == 'b' and s2[i+1] == 'a':
                    s2 = s2[:i] + s2[i+2:]
                    ans += y
                    i = max(i - 1, 0)
                else:
                    i += 1

            i = 0
            while i < len(s2) - 1:
                if s2[i] == 'a' and s2[i+1] == 'b':
                    s2 = s2[:i] + s2[i+2:]
                    ans += x
                    i = max(i - 1, 0)
                else:
                    i += 1

        return ans
