class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        else:
            d = {}
            r = {}  # reverse mapping dictionary
            for i in range(len(s)):
                if s[i] not in d:
                    # if t[i] already mapped by another s character, fail
                    if t[i] in r and r[t[i]] != s[i]:
                        return False
                    d[s[i]] = t[i]
                    r[t[i]] = s[i]
                else:
                    if d[s[i]] == t[i]:
                        continue
                    else:
                        return False

        return True
