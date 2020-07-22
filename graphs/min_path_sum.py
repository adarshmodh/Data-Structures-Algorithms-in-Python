"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7

Multiple solutions possible based on DP-

If you cannot change values in the matrix, 
Time Complexity - O(mn)
Space Complexity - O(mn)
Basically create another matrix of the same shape and store the minimum path sum values in it.


if editing the matrix is allowed, then the solution below
Time Complexity - O(mn)
Space Complexity - O(1)

"""

def minPathSum(grid):
    m = len(grid)
    n = len(grid[0])
    for i in range(1, n):
        grid[0][i] += grid[0][i-1]
       
    for i in range(1, m):
        grid[i][0] += grid[i-1][0]
    
    
    for i in range(1, m):
        for j in range(1, n):
            grid[i][j] += min(grid[i-1][j], grid[i][j-1])
    
    return grid[-1][-1]

grid = [[1,3,1],[1,5,1],[4,2,1]]

print(minPathSum(grid))