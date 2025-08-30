class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                char = board[i][j]
                if char != '.':
                    box_index = (i // 3) * 3 + (j // 3)
                    
                    if char in rows[i] or char in cols[j] or char in boxes[box_index]:
                        return False
                    
                    rows[i].add(char)
                    cols[j].add(char)
                    boxes[box_index].add(char)
        
        return True