"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

"""

def threeSum(nums, target):
    res = []
    nums.sort()

    for i in range(len(nums)):
        
        if nums[i] > 0:  ##### because sorted array further elements will be higher than zero
            break
        
        tmp = twoSumSorted(nums[i+1:], target-nums[i])
        if tmp[0]!=-1:
            res.append([nums[i],nums[tmp[0]+i],nums[tmp[1]+i]])

    return res


def twoSumSorted(numbers, target):        
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    low = 0
    high = len(numbers)-1
    
    while(low<high):
        curr_sum = numbers[low] + numbers[high]
        
        if curr_sum == target:
            return [low+1, high+1]
        elif curr_sum < target:
            low += 1
        else:
            high -= 1
   
    return [-1,-1]


nums = [-1, 0, 1, 2, -1, -4]
target = 0

print(threeSum(nums, target))
