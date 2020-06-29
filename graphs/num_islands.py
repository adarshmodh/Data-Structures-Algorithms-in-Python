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
        grid[i][j] = '#'
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
