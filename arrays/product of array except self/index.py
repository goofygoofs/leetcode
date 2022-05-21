'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

'''

'''
nums = [1,2,3,4]
prefix - [1,2,6,24]
postfix - [24,24,12,4]
first position has no prefix multiplification (use 1)
output = [1, 1, 2, 6]
         [1*4*3*2=24, 1*4*3=12, 2*4=8, 6*1]
         [24,12,8,6]
'''

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1]
        tmp = 1
        # prefix
        for i in range(len(nums) - 1): #i=0, this is prefix for j=1
            tmp *= nums[i]
            output.append(tmp)
        #postfix
        tmp = 1
        for i in range(len(nums)-2,-1,-1): # skip the last one because last one does not have any postfix after it
            tmp *= nums[i+1]
            output[i] *= tmp
        return output

sol = Solution()
output = sol.productExceptSelf([1,2,3,4])
print(output)
