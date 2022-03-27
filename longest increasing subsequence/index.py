'''
Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. 
For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

 

Example 1:

Input: nums = [10,3,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1
 

Constraints:

1 <= nums.length <= 2500
-104 <= nums[i] <= 104
'''

'''
store the current smallest number
smallest = 2
{
    10: [10]
    9: [9]
    3: [3, 4, 5, 6,7]
    2: [0,7]
    1: [1,2]
    2: [2]
}
brute force method On^2


'''
from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = 0
        for i, num in enumerate(nums):
            longestSequence = {num: [num]}
            for i2 in range(i+1, len(nums)):
                if nums[i2] not in longestSequence:
                    longestSequence[nums[i2]] = [nums[i2]]
                for key in longestSequence:
                    if nums[i2] > longestSequence[key][-1]:
                        longestSequence[key].append(nums[i2])
                        
            print('longestSeuqence', longestSequence)
            for key in longestSequence:
                LIS = max(LIS, len(longestSequence[key]))
        return LIS

solution = Solution()
output = solution.lengthOfLIS([10,3,9,2,5,3,7,101,18])
print(output)

output = solution.lengthOfLIS([0,1,0,3,2,3])
print(output)