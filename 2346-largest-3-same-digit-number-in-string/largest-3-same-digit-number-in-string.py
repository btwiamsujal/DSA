class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        ans = []
        for i in range(2, len(num)):
            if num[i-2] == num[i-1] == num[i]:
                ans.append(num[i])
        if not ans:
            return ""
        m = max(ans)
        return m * 3