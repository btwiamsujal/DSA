class Solution:
    def lenOfVDiagonal(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
        
        end_dp = [[[0] * n for _ in range(m)] for _ in range(4)]
        start_dp = [[[0] * n for _ in range(m)] for _ in range(4)]
        
        for d in range(4):
            dx, dy = directions[d]
            if d == 0:
                for i in range(m):
                    for j in range(n):
                        if grid[i][j] == 1:
                            end_dp[d][i][j] = 1
                        elif grid[i][j] == 2:
                            pi, pj = i - dx, j - dy
                            if 0 <= pi < m and 0 <= pj < n and (grid[pi][pj] == 1 or grid[pi][pj] == 0) and end_dp[d][pi][pj] > 0:
                                end_dp[d][i][j] = end_dp[d][pi][pj] + 1
                            else:
                                end_dp[d][i][j] = 0
                        elif grid[i][j] == 0:
                            pi, pj = i - dx, j - dy
                            if 0 <= pi < m and 0 <= pj < n and grid[pi][pj] == 2 and end_dp[d][pi][pj] > 0:
                                end_dp[d][i][j] = end_dp[d][pi][pj] + 1
                            else:
                                end_dp[d][i][j] = 0
                        else:
                            end_dp[d][i][j] = 0
            elif d == 1:
                for i in range(m):
                    for j in range(n-1, -1, -1):
                        if grid[i][j] == 1:
                            end_dp[d][i][j] = 1
                        elif grid[i][j] == 2:
                            pi, pj = i - dx, j - dy
                            if 0 <= pi < m and 0 <= pj < n and (grid[pi][pj] == 1 or grid[pi][pj] == 0) and end_dp[d][pi][pj] > 0:
                                end_dp[d][i][j] = end_dp[d][pi][pj] + 1
                            else:
                                end_dp[d][i][j] = 0
                        elif grid[i][j] == 0:
                            pi, pj = i - dx, j - dy
                            if 0 <= pi < m and 0 <= pj < n and grid[pi][pj] == 2 and end_dp[d][pi][pj] > 0:
                                end_dp[d][i][j] = end_dp[d][pi][pj] + 1
                            else:
                                end_dp[d][i][j] = 0
                        else:
                            end_dp[d][i][j] = 0
            elif d == 2:
                for i in range(m-1, -1, -1):
                    for j in range(n-1, -1, -1):
                        if grid[i][j] == 1:
                            end_dp[d][i][j] = 1
                        elif grid[i][j] == 2:
                            pi, pj = i - dx, j - dy
                            if 0 <= pi < m and 0 <= pj < n and (grid[pi][pj] == 1 or grid[pi][pj] == 0) and end_dp[d][pi][pj] > 0:
                                end_dp[d][i][j] = end_dp[d][pi][pj] + 1
                            else:
                                end_dp[d][i][j] = 0
                        elif grid[i][j] == 0:
                            pi, pj = i - dx, j - dy
                            if 0 <= pi < m and 0 <= pj < n and grid[pi][pj] == 2 and end_dp[d][pi][pj] > 0:
                                end_dp[d][i][j] = end_dp[d][pi][pj] + 1
                            else:
                                end_dp[d][i][j] = 0
                        else:
                            end_dp[d][i][j] = 0
            elif d == 3:
                for i in range(m-1, -1, -1):
                    for j in range(n):
                        if grid[i][j] == 1:
                            end_dp[d][i][j] = 1
                        elif grid[i][j] == 2:
                            pi, pj = i - dx, j - dy
                            if 0 <= pi < m and 0 <= pj < n and (grid[pi][pj] == 1 or grid[pi][pj] == 0) and end_dp[d][pi][pj] > 0:
                                end_dp[d][i][j] = end_dp[d][pi][pj] + 1
                            else:
                                end_dp[d][i][j] = 0
                        elif grid[i][j] == 0:
                            pi, pj = i - dx, j - dy
                            if 0 <= pi < m and 0 <= pj < n and grid[pi][pj] == 2 and end_dp[d][pi][pj] > 0:
                                end_dp[d][i][j] = end_dp[d][pi][pj] + 1
                            else:
                                end_dp[d][i][j] = 0
                        else:
                            end_dp[d][i][j] = 0
        
        for d in range(4):
            dx, dy = directions[d]
            if d == 0:
                for i in range(m-1, -1, -1):
                    for j in range(n-1, -1, -1):
                        if grid[i][j] not in (0, 1, 2):
                            start_dp[d][i][j] = 0
                        else:
                            next_val = 2 if grid[i][j] in (1, 0) else 0
                            ni, nj = i + dx, j + dy
                            if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == next_val:
                                start_dp[d][i][j] = 1 + start_dp[d][ni][nj]
                            else:
                                start_dp[d][i][j] = 1
            elif d == 1:
                for i in range(m-1, -1, -1):
                    for j in range(n):
                        if grid[i][j] not in (0, 1, 2):
                            start_dp[d][i][j] = 0
                        else:
                            next_val = 2 if grid[i][j] in (1, 0) else 0
                            ni, nj = i + dx, j + dy
                            if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == next_val:
                                start_dp[d][i][j] = 1 + start_dp[d][ni][nj]
                            else:
                                start_dp[d][i][j] = 1
            elif d == 2:
                for i in range(m):
                    for j in range(n):
                        if grid[i][j] not in (0, 1, 2):
                            start_dp[d][i][j] = 0
                        else:
                            next_val = 2 if grid[i][j] in (1, 0) else 0
                            ni, nj = i + dx, j + dy
                            if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == next_val:
                                start_dp[d][i][j] = 1 + start_dp[d][ni][nj]
                            else:
                                start_dp[d][i][j] = 1
            elif d == 3:
                for i in range(m):
                    for j in range(n-1, -1, -1):
                        if grid[i][j] not in (0, 1, 2):
                            start_dp[d][i][j] = 0
                        else:
                            next_val = 2 if grid[i][j] in (1, 0) else 0
                            ni, nj = i + dx, j + dy
                            if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == next_val:
                                start_dp[d][i][j] = 1 + start_dp[d][ni][nj]
                            else:
                                start_dp[d][i][j] = 1
        
        ans = 0
        for i in range(m):
            for j in range(n):
                for d in range(4):
                    if end_dp[d][i][j] > ans:
                        ans = end_dp[d][i][j]
                    next_d = (d + 1) % 4
                    if end_dp[d][i][j] > 0 and start_dp[next_d][i][j] > 0:
                        total = end_dp[d][i][j] + start_dp[next_d][i][j] - 1
                        if total > ans:
                            ans = total
        return ans