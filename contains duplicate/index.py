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

'''
brute force is O(n^2) comparing each number . this approach would be O(1) space since we do use any extra space

another way is sorting and iterating through the array once. and checking neighbors and shifting pointers. sorting takes extra time so it's O(nlogn). but we don't need extra space if you don't count space by sorting algo.

if we don't sort, we use extra memory - we use a hash set. we can insert into hash set in O(1) time and lookup in O(1) time

best case is using hash set and time and space complexity is O(n).
 
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