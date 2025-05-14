"""
A set S of n integers originally contains all of the numbers from 1 to n (and no other numbers). Due to corruption, exactly one of the numbers in the set S is duplicated onto another number in the set. The corrupted set has the integers 1 to n, with one number repeated and one missing number. Neither the original nor the corrupted sets are guaranteed to be in order. The original array is not given to us. Write a function which takes an integer array of arbitrary length at runtime (the corrupted set) as input, and returns the duplicated number and the missing number as an array. 
"""

from typing import List

def find_duplicate_and_missing(nums: List[int]) -> List[int]:
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    expected_square_sum = sum(i * i for i in range(1, n + 1))
    
    actual_sum = sum(nums)
    actual_square_sum = sum(x * x for x in nums)
    
    sum_diff = expected_sum - actual_sum  # missing - duplicate
    square_sum_diff = expected_square_sum - actual_square_sum  # missing^2 - duplicate^2
    
    missing_plus_duplicate = square_sum_diff // sum_diff  # (missing + duplicate)
    
    missing = (sum_diff + missing_plus_duplicate) // 2
    duplicate = missing_plus_duplicate - missing
    
    return [duplicate, missing]

# Example usage:
numbers = [4, 3, 2, 7, 8, 2, 6, 1]
print(find_duplicate_and_missing(numbers))
