def dfs(i,j,grid):
    
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]) or grid[i][j] == 0:
        return 0
    
    grid[i][j] = 0
    
    up = dfs(i,j+1,grid)
    down = dfs(i,j-1,grid)
    left = dfs(i-1,j,grid)
    right = dfs(i+1,j,grid)
    
    return up + down + left + right + 1

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                
                if grid[i][j] == 1:
                    count = max(dfs(i,j,grid), count)
                    
        return count






#####################BFS 


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        area = 0

        def bfs(r, c):
            q = deque()
            grid[r][c] = 0
            q.append((r, c))
            res = 1

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if (nr < 0 or nc < 0 or nr >= ROWS or
                        nc >= COLS or grid[nr][nc] == 0
                    ):
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = 0
                    res += 1
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = max(area, bfs(r, c))

        return area
