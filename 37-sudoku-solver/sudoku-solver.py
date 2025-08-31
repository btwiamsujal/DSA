class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # Create sets to keep track of numbers in each row, column, and 3x3 box
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        # Populate the sets with the initial board state
        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    num = board[r][c]
                    box_id = (r // 3) * 3 + (c // 3)
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[box_id].add(num)
        
        def backtrack(r, c):
            # Base case: If we've moved past the last row, the puzzle is solved
            if r == 9:
                return True
            
            # Calculate the next cell's coordinates
            next_r, next_c = (r, c + 1) if c < 8 else (r + 1, 0)

            # If the current cell is already filled, move to the next one
            if board[r][c] != '.':
                return backtrack(next_r, next_c)
            
            # Try placing numbers 1-9 in the empty cell
            for num_char in "123456789":
                box_id = (r // 3) * 3 + (c // 3)
                if num_char not in rows[r] and num_char not in cols[c] and num_char not in boxes[box_id]:
                    # Place the number
                    board[r][c] = num_char
                    rows[r].add(num_char)
                    cols[c].add(num_char)
                    boxes[box_id].add(num_char)
                    
                    if backtrack(next_r, next_c):
                        return True
                    board[r][c] = '.'
                    rows[r].remove(num_char)
                    cols[c].remove(num_char)
                    boxes[box_id].remove(num_char)
            
            return False
            
        backtrack(0, 0)