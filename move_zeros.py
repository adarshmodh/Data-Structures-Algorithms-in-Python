
"""
Best solution 2 pointer approach 

Time complexity = O(n)
Space complexity = O(1)

read - fast, write - slow

Working through an example, say we have an array [1, 0, 2, 0, 3].

When read = 0, write = 0 and write += 1.
When read = 1, then array[read] == 0 and write = 1.
When read = 2, then we swap array[2] (read) and array[1] (write). The array is now [1, 2, 0, 0, 3] and write = 2.
When read = 3, array[read] == 0 and we skip.
When read = 4, then we swap array[4] (read) and array[2] (write). The final array is [1, 2, 3, 0, 0].


"""

def move_zeros(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
#         n = len(nums)
#         cntr = 0
#         zeros = 0
#         while cntr<(n-zeros):
#             if nums[cntr] == 0:
#                 nums.pop(cntr)
#                 nums.append(0)
#                 zeros += 1
#             else:
#                 cntr += 1
            
#         return nums
    
    zero = 0  # records the position of "0"
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[zero] = nums[zero], nums[i]
            zero += 1

    return nums

arr = [1, 10, 0, 2, 8, 3, 0, 0, 6, 4, 0, 5, 7, 0]
print(move_zeros(arr))

