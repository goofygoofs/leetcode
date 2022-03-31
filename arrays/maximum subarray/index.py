'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
                       L/  R
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
 

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

'''

'''
i think we want to do a 2 pointer solution. based on some conditions we will move the pointer over
we want the most positive number
if leftPointer is higher starting at index i than sum of all values from LeftPointer to RightPointer?, move over leftPointer
rightPointer, store lastHighestValue and index from rightPointer 

O(n) time complexity
O(1) space because we just use a few variables

what if there's a lot of 0?, do we include the 0 or no?

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
                       L/  R

what if array is all negative?
'''
from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        leftPointer = 0
        rightPointer = 0
        maxValue = nums[0]
        # create temp for holding previous value to compare to current value to avoid calling sum every iteration andd increasing time complexity
        prev = nums[0]

        if len(nums) == 1:
            return maxValue

        for i, num in enumerate(nums):
            if i == 0:
                continue
            leftValue = nums[leftPointer]
            rightValue = nums[rightPointer]

            curr = prev + num

            # right side
            if curr > prev:
                rightPointer = i
                

            # left side
            if num > curr:
                leftPointer = i
                rightPointer = i
            # print('curr', curr, 'i', i, 'num', num, 'leftPointer', leftPointer, 'rightPointer', rightPointer)
            if leftPointer != i:
                prev = curr
            else:
                prev = num

            maxValue = max(maxValue, prev)
            # print('prev', prev, 'maxValue', maxValue)

        return maxValue

# sol = Solution()

# output = sol.maxSubArray([-2,-1])
# print(output)

# output = sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
# print(output)

# output = sol.maxSubArray([1])
# print(output)

# output = sol.maxSubArray([5,4,-1,7,8])
# print(output)