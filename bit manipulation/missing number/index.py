'''
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

 

Example 1:

Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
Example 2:

Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
Example 3:

Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
 

Constraints:

n == nums.length
1 <= n <= 104
0 <= nums[i] <= n
All the numbers of nums are unique.
 

Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?
'''

'''
we are given an array of n distinct numbers in range [0, n+1], we're only choosing n distinct numbers in this range
we want only missing nuimber
can we do this using O(1) extra space and O(n) runtime?
[0,3] 0,1,2,3
nums = [3, 0, 1] => output = 2
missing number is 2
you can think of 0,1,2,3 as a hashset/hashmap and iterate through list of nums
and crossing out the ones that are already contained in the input
O(n) extra memory because of hashmap/set
and O(n) time to iterate through array input

followup to do in O(1) memory?
gonna need binary properties
XOR operation. exclusive OR operator
(2 ^ 3)
10 => 2
11 => 3
---
01 - if they are different, will return a 1. if same returns a 0
01 => 1
(5 ^ 5)
101
101
----
000 (exact same)
the order in which we XOR does not matter
(5^5^3) since (5^5) is 0 => (0^3)
011 => 3
000 => 0
----
011 => 3
so we are gonna take this range [0,1,2,3] and exclusive XOR it with [0,1,3]
so this will give us only [2]

we can also take the sum of each array and subtract it from each other
this also is O(1) memory
sum can actually be O(1) time using gauses' formula
''' 

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # after subtracting from the loops below, will have missing number
        res = len(nums)

        for i in range(len(nums)):
            # we want to add it then subtract the i'th from num
            # because we gonna subtract the sum of the nums list anyways
            # this will give us the missing number
            res += (i - nums[i])
        return res