'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

'''

'''
O(n) run 1 pass through?
'''
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        integersSeenSoFar = {}

        for i, num in enumerate(nums): # 0, 2
            if num not in integersSeenSoFar: # 2
                integersSeenSoFar[target-num] = i # 9-2 => {7:0}
            else:
                return [integersSeenSoFar[num], i] # return previous and current index

        return [-1, -1]


solution = Solution()

output = solution.twoSum([2,7,11,15], 9)
print(output)

output = solution.twoSum([3,2,4], 6)
print(output)

output = solution.twoSum([3,3], 6)
print(output)

output = solution.twoSum([3,3], 66)
print(output)

# o(n) it is 1 time pass through, we're looping through the list which is o(n). lookup on hash table is o(1)
# o(n) space because of hash table