class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        """
        :type fruits: List[int]
        :type baskets: List[int]
        :rtype: int
        """
        n = len(fruits)
        used = [False] * n
        placed = 0

        for x in fruits:
            for i in range(n):
                if not used[i] and baskets[i] >= x:
                    used[i] = True
                    placed += 1
                    break

        return n - placed
