'''
Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.

 

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 

Constraints:

1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
'''

'''
product = multiplication
can have negatives
base cases: 0, negatives
O(n) time  
O(1) space (using input array)

going through and updating each value iwth the maximum at that index so far

[2,3,-2,4]
    [2,6,-2,4]
[-2,2,3,-2]
    [-2,2,6,-2]

brute force
-2,-4,-12,24
...
24,...
O(n^2) time
'''

'''
if we have positive numbers,
no matter what the highest number would keep increasing to the right
Q: how about all negatives?
negative consecutively, the sign is alternating
if we want to find the max prod subarray we need to keep track of the min
[-1,-2,-3]
for -1,-2 the max product subarray is 2 (-1*-2) and min is -2 (just -2)
2|-2
max|min
-3 * 2 = -6 (min)
-3 * -2 = 6 (max)
 1 is a neutral value so it won't kill the product subarray

[2,3,0,4]
curMax = 6
curMin = 0

res variable keeps track of previous contiguous subarray in case of 0's
'''

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # O(n) / O(1) : Time / Memory
        res = max(nums)
        curMin, curMax = 1, 1 # beacuse 1 is a neutral value

        for n in nums:
            tmp = curMax * n
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(tmp, n * curMin, n)
            print('currMax', curMax, 'curMin', curMin)
            res = max(res, curMax)
        return res

sol = Solution()
output = sol.maxProduct([2,3,0,4])
print(output)