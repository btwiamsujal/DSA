class Solution(object):
    def sortMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(grid)
        diagonals = {}
        for i in range(n):
            for j in range(n):
                d = i - j
                if d not in diagonals:
                    diagonals[d] = []
                diagonals[d].append(grid[i][j])

        for d in diagonals:
            if d >= 0:  
                diagonals[d].sort(reverse=True)  
            else:      
                diagonals[d].sort()  

        for i in range(n):
            for j in range(n):
                d = i - j
                grid[i][j] = diagonals[d].pop(0)

        return grid