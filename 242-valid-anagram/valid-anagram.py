class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        else:
            for l in set(s):
                if (s.count(l) != t.count(l)):
                    return False
            return True