'''
Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
'''

'''
set O(1) look up
O(n) time complexity still because looping through nums. but can exit early if duplicate detected early
so O(n - k)
O(n - k) space complexity too depending on how early dup is found
'''
from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                return True
        return False

sol = Solution()

output = sol.containsDuplicate([1,2,3,1])
print(output)

output = sol.containsDuplicate([1,2,3,4])
print(output)

output = sol.containsDuplicate([1,1,1,3,3,4,3,2,4,2])
print(output)