class Solution:
    def numIslands(self, grid):

        if not grid:
            return 0

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    # print(grid)
                    count += 1
        
        # print(grid)
        
        return count

    def dfs(self, grid, i, j):
        
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '#' # Mark as visited
            # Explore all 4 directions
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)

mapof_islands = [["1","1","0","0","0"],\
                ["1","1","0","0","0"],\
                ["0","0","1","0","0"],\
                ["0","0","0","1","1"]]

print(mapof_islands)
islands = Solution()

print(islands.numIslands(mapof_islands))



###BFS Approach
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        island_count = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Right, Left, Down, Up
        
        def bfs(r, c):
            queue = deque([(r, c)])
            grid[r][c] = "0"  # Mark as visited
            while queue:
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == "1":
                        queue.append((nx, ny))
                        grid[nx][ny] = "0"  # Mark as visited
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":  # Found a new island
                    island_count += 1
                    bfs(r, c)  # Perform BFS to mark the entire island
        
        return island_count
