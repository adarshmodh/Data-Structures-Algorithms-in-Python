"""
You are given a 0-indexed integer array nums. There exists an array arr of length nums.length, where arr[i] is the sum of |i - j| over all j such that nums[j] == nums[i] and j != i. If there is no such j, set arr[i] to be 0.

Return the array arr.

Example 1:

Input: nums = [1,3,1,1,2]
Output: [5,0,3,4,0]
Explanation: 
When i = 0, nums[0] == nums[2] and nums[0] == nums[3]. Therefore, arr[0] = |0 - 2| + |0 - 3| = 5. 
When i = 1, arr[1] = 0 because there is no other index with value 3.
When i = 2, nums[2] == nums[0] and nums[2] == nums[3]. Therefore, arr[2] = |2 - 0| + |2 - 3| = 3. 
When i = 3, nums[3] == nums[0] and nums[3] == nums[2]. Therefore, arr[3] = |3 - 0| + |3 - 2| = 4. 
When i = 4, arr[4] = 0 because there is no other index with value 2. 

Example 2:

Input: nums = [0,5,3]
Output: [0,0,0]
Explanation: Since each element in nums is distinct, arr[i] = 0 for all i.

Time and space complexity - O(n)
"""

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)
        
        # use defaultdict(int) instead of normal dict to not have errors for uninitialized keys 
        sum_left = defaultdict(int)   # sum of indices on the left 
        cnt_left = defaultdict(int)   # number of occurences on the left 
        
        for i, x in enumerate(nums):
            output[i] += cnt_left[x] * i   # the current index is the highest if you look from the left, so sum on the left is (idx * occurences - (sum of previous idxs))
            output[i] -= sum_left[x]

            cnt_left[x] += 1
            sum_left[x] += i
        
        sum_right = defaultdict(int)
        cnt_right = defaultdict(int)
        
        for i, x in reversed(list(enumerate(nums))):
            output[i] += sum_right[x]        # similarly, the current idx is the lowest if you look from right, the sum on the right is  ( (sum of subsequent idxs) - idx * occurences)
            output[i] -= cnt_right[x] * i

            cnt_right[x] += 1
            sum_right[x] += i

        return output
