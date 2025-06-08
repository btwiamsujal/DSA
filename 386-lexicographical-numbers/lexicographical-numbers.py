class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = []
        for i in range(1, n+1):
            k = str(i)
            ans.append(k)
        ans.sort()
        return list(map(int ,ans))
