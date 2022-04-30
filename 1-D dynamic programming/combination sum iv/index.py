'''
Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.

The test cases are generated so that the answer can fit in a 32-bit integer.

 

Example 1:

Input: nums = [1,2,3], target = 4
Output: 7
Explanation:
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
Note that different sequences are counted as different combinations.
Example 2:

Input: nums = [9], target = 3
Output: 0
 

Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 1000
All the elements of nums are unique.
1 <= target <= 1000
 

Follow up: What if negative numbers are allowed in the given array? How does it change the problem? What limitation we need to add to the question to allow negative numbers?

'''

'''

'''

from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = {0: 1} # 1 way to reach 0
        for total in range(1, target + 1): # go up to including target, we already done 0
            dp[total] = 0
            # print('dp', dp, 'total', total)
            for num in nums:
                # at total = 2 and num = 1, we already caculated 2-1 = 1 and we know for 1, we calculated (1-1 =0, 1 way)
                # so {2: 1}
                # then total = 2 and num = 2, we calculated 2-2=0 (another 1 way)
                # {2: 2} 
                # at total = 3, and num = 1 (3-1=2) and at 2 we calcuated 2 ways
                # {3:2}
                # total = 3 num = 2 (3-2=1) (1 way)
                # 3:3
                # total = 3 num = 3 (3-3=0) (1 way)
                # {3: 4}
                dp[total] += dp.get(total-num, 0) # if exists get dp[total - num] else return 0
                # print('updated', dp, 'num', num)
        return dp[target]

# sol = Solution()
# output = sol.combinationSum4([1,2,3], 4)
# print(output)