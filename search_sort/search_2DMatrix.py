"""
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        high = len(matrix) - 1

        while low <= high:
            mid = (low + high) //2
            
            if matrix[mid][0] == target: 
                return True 
            
            elif target < matrix[mid][0]:
                high =  mid - 1
            
            else:
                low = mid + 1
        
        row_select = high
        
        low = 0
        high = len(matrix[row_select]) - 1
        while low <= high:
            mid = (low + high) //2
            
            if matrix[row_select][mid] == target: 
                return True 
            
            elif target < matrix[row_select][mid]:
                high =  mid - 1
            
            else:
                low = mid + 1
        
        return False
