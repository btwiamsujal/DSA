class Solution(object):
    def maxTotalFruits(self, fruits, startPos, k):
        """
        :type fruits: List[List[int]]
        :type startPos: int
        :type k: int
        :rtype: int
        """
        n = len(fruits)
        max_fruits = 0
        i = 0
        total = 0

        for j in range(n):
            total += fruits[j][1]

            while i <= j:
                left = fruits[i][0]
                right = fruits[j][0]

                min_steps = min(
                    abs(startPos - left) + (right - left),
                    abs(startPos - right) + (right - left)
                )

                if min_steps > k:
                    total -= fruits[i][1]
                    i += 1
                else:
                    break

            max_fruits = max(max_fruits, total)

        return max_fruits