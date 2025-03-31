from collections import deque

class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        island_count = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Down, Up, Right, Left
        
        def dfs(r,c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != "1": # checking if its zero or #
                return 
            
            grid[r][c] = "#"

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        
        def bfs(r, c):
            queue = deque([(r, c)])
            grid[r][c] = "0"  # Mark as visited

            while queue:
                x, y = queue.popleft()  # Dequeue the front element
                
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy  # Calculate new coordinates
                    
                    # Check if it's within bounds and is land
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == "1":
                        queue.append((nx, ny))  # Add to queue
                        grid[nx][ny] = "0"  # Mark as visited

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":  # Found an island
                    island_count += 1
                    bfs(r, c)  # Perform BFS to mark all connected land cells

        return island_count
