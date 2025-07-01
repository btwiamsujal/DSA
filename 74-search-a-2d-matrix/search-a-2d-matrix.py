class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for i in range(len(matrix)):
            if(matrix[i][-1]) < target:
                continue
            else:
                for j in range(0, len(matrix[i])):
                    if matrix[i][j] == target:
                        return True
                return False
        return False