class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ans1 = ''.join(sorted(s))
        ans2 = ''.join(sorted(t))
        if ans1 == ans2:
            return True
        else:
            return False
        