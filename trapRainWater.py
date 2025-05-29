"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9
"""


def trap_at_i(height, i):
    #less optimal approach O(n^2), call this function for each idx in the array 
    if not height or i <= 0 or i >= len(height) - 1:
        return 0  # No water trapped at edges

    max_left = max(height[:i+1])
    max_right = max(height[i:])
    return max(0, min(max_left, max_right) - height[i])


def trap(height: List[int]) -> int:
    #mid optimal approach time - O(n), space O(n), precompute max_left and max_right for each step 
    if not height:
        return 0

    n = len(height)
    max_left = [0] * n
    max_right = [0] * n

    # Fill max_left: highest wall to the left of i (including i)
    max_left[0] = height[0]
    for i in range(1, n):
        max_left[i] = max(max_left[i - 1], height[i])

    # Fill max_right: highest wall to the right of i (including i)
    max_right[n - 1] = height[n - 1]
    for i in range(n - 2, -1, -1):
        max_right[i] = max(max_right[i + 1], height[i])

    # Calculate trapped water
    water_trapped = 0
    for i in range(n):
        water_trapped += max(0, min(max_left[i], max_right[i]) - height[i])

    return water_trapped
