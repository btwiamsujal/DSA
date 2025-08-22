class Solution(object):
    def minimumArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n, m = len(grid), len(grid[0])
        min_row, max_row = n, -1
        min_col, max_col = m, -1

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    min_row = min(min_row, i)
                    max_row = max(max_row, i)
                    min_col = min(min_col, j)
                    max_col = max(max_col, j)

        if max_row == -1:  
            return 0  

        height = max_row - min_row + 1
        width = max_col - min_col + 1
        return height * width
        