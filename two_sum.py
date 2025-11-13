"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""


def twoSum(nums, target):        
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    # two pass solution ( time and space complexity - O(n))
    indices = {} 

    for i in range(len(nums)): # store all the numbers in nums in a dict with their indices
        indices[nums[i]] = i

    for j in range(len(nums)): # iterate through nums to see if there is a diff (target - nums[j]) that exists (while making sure i!=j)
        diff = target - nums[j]
        if diff in indices and indices[diff] != j:
            return [j, indices[diff]]
    
    return []

nums = [2, 7, 11, 15]
target = 9

print(twoSum(nums,target))

