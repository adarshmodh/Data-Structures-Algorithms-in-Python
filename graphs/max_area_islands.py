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