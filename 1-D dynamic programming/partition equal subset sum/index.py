'''
Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

 

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
 

Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 100
'''

'''
1 array and patition it into 2 subsets that have equal sums

sort => increment left and right poitner
[1,5,5,11]
        L      
     6
     L<R
Q: do we have to use entire array? probably yes
'''

'''
if we sum up the entire array and divide by 2, do we ever get that number. 
so we sum up, we get 22, 22/2 = 11. do we ever get 11?
for each number we have 2 decisions: chose that number to sum, or not choose it
             [1,5,5,11]
                |
            |   |
            1   0
          | |   | |
          6 1   5 0
          ....
if we can find 1 subset that equals 11, the sum of the others must be 11
when we move i over, we look at the remaining subarray minus the 1st index
we can cache this
[1,5,11,5]

[1] [5,11,5]
      | |
      1 0
target=10 target=11
i=1         i=1
target is sum(array) / 2
this is better than 2^n


bottom up soln
how many sums at the last position? 0 or 5
then at the next index 11, add it to our set
{0,5,11,16}
5
{0,5,10,11,16,21}
1
{0,5,6,11,12,17,22} this is entire list of sums we can create
time - O(n * sum(nums))
space - O(sum(nums))
'''

from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # if sum is odd, it's impossible to partition it
        if sum(nums)%2 == 1:
            return False
        
        dp = set()
        dp.add(0) # add 0 because we can take the value or not
        target = sum(nums) / 2

        for i in range(len(nums)-1,-1,-1):
            nextDp = set()
            for totalValues in dp:
                tmp = totalValues + nums[i]
                if tmp == target: # if we find target, other subarray must sum up to target too
                    return True
                nextDp.add(totalValues + nums[i])
                nextDp.add(totalValues)
            dp = nextDp
        return True if target in dp else False

