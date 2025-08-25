class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        rows = len(mat)
        cols = len(mat[0])

        res = []

        cur_row = cur_col = 0
        going_up = True

        while len(res) != rows * cols:
            if going_up:
                while cur_row >= 0 and cur_col < cols:
                    res.append(mat[cur_row][cur_col])

                    cur_row -= 1
                    cur_col += 1

                if cur_col == cols:
                    cur_row += 2
                    cur_col -= 1
                else:
                    cur_row += 1
                
                going_up = False
            
            else:
                while cur_col >= 0 and cur_row < rows:
                    res.append(mat[cur_row][cur_col])

                    cur_col -= 1
                    cur_row += 1

                if cur_row == rows:
                    cur_col += 2
                    cur_row -= 1
                else:
                    cur_col += 1
                
                going_up = True

        return res
