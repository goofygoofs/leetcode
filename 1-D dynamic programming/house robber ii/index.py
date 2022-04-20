'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
Example 2:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 3:

Input: nums = [1,2,3]
Output: 3
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 1000
'''

'''
the front and back of the array are circle (connected), so cannot rob both front and back
[2,3,2]
[0,0,0]
if it's 3 or below, rob max(arr)

[1,2,3,4]
[1,2,3,6]
[1,3,1,3,1,3,5]
[1,3,1,6,4,9,11]

look at previous 2 (skipping most adjacent)
'''

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 4:
            return max(nums)
        
        dp = [0] * len(nums)
        # max(nums[2], nums[2]+nums[0]) fixes case for length 4 
        dp[0],dp[1],dp[2] = nums[0],nums[1],nums[2]

        for i in range(2, len(nums)):
            # edge case if we only use index 0 and 2
            if i == 2:
                dp[i] = dp[i-2] + nums[i]
                continue
            if i == len(nums) - 1:
                if i % 2 == 0: # odd number so last house has conditions on whether or not to use first home
                    dp[i] = max(dp[i-3] + nums[i], dp[i-2]) # can't use last house or use 3rd from last with last house
                    break

            dp[i] = max(dp[i-3] + nums[i], dp[i-2] + nums[i])
        
        return max(dp[-2], dp[-1])
