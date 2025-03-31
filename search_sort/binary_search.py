"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(arr, x):
    """Your code goes here."""
    
    l = 0
    r = len(arr)-1
    
    while l <= r: 
  
        mid = l + (r - l)//2; 
          
        # Check if x is present at mid 
        if arr[mid] == x: 
            return mid 
  
        # If x is greater, ignore left half 
        elif arr[mid] < x: 
            l = mid + 1
  
        # If x is smaller, ignore right half 
        else: 
            r = mid - 1
      
    # If we reach here, then the element was not present 
    return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)


"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity. 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4

"""
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """Your code goes here."""
    
        l = 0
        r = len(nums)-1
        
        while l <= r: 
    
            mid = l + (r - l)//2; 
            
            # Check if x is present at mid 
            if nums[mid] == target: 
                return mid 
    
            # If x is greater, ignore left half 
            elif nums[mid] < target: 
                l = mid + 1
    
            # If x is smaller, ignore right half 
            else: 
                r = mid - 1
        
        # If we reach here, then the element was not present 
        if target < nums[mid]:
            return mid
        else:
            return mid+1
