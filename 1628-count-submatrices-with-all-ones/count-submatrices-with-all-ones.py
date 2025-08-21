class Solution(object):
    def numSubmat(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        rows, cols = len(mat), len(mat[0])
        height = [[0]*cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 1:
                    height[i][j] = height[i-1][j] + 1 if i > 0 else 1

        result = 0
        for i in range(rows):
            for j in range(cols):
                if height[i][j] > 0:
                    min_height = height[i][j]
                    k = j
                    while k >= 0 and height[i][k] > 0:
                        min_height = min(min_height, height[i][k])
                        result += min_height
                        k -= 1
        return result

