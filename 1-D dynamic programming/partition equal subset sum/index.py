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
[1,5,5,6,11]
        L      
     6
     L<R
Q: do we have to use entire array? probably yes
'''

from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return False
        nums.sort()
        l = 0
        r = len(nums)-1
        ltotal = nums[l]
        rtotal = nums[r]
        
        while l < r-1:
            if ltotal <= rtotal:
                l += 1
                ltotal += nums[l]
            elif ltotal > rtotal:
                r -= 1
                rtotal += nums[r]
        print(ltotal, rtotal)
        return ltotal == rtotal            

sol = Solution()
output = sol.canPartition([1,5,11,5])
print(output)