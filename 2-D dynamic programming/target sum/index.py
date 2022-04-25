'''
You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.

 

Example 1:

Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
Example 2:

Input: nums = [1], target = 1
Output: 1
 

Constraints:

1 <= nums.length <= 20
0 <= nums[i] <= 1000
0 <= sum(nums[i]) <= 1000
-1000 <= target <= 1000
'''

'''
build amount of different assignments possible to get target

Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3

position does matter
have 4(+1) and 1(-1) all in different positions

                target
            3   2   1   0
nums
    1
    1
    1
    1       6   3   1   0
    1       3   2   1   0
'''

'''
brute force - 2^n
every single value we have 2 choices, add or minus and can visualize as a decision tree
(index, total)
                    (0,0)
                    |+1   |-1
                (1,1)   (1,-1)
                .....
can use caching to optimize
maximum total is sum of array = 5
minimum is -5 since if we subtract every number = -5
[-5,5] every value between these
O(n*t) t is sum of entire array. n is number of nums
O(n*t) space for dp and recursive stack
we use dp dict with (index, total) starting at 0,0
then when we reach the end if total == target, we return 1 in dp for that Tuple(index,total) in dictionary
we take the + addition and - subtracktion and add them together to get the unique permutation counts
set equal to dict[(0,0)]
'''

from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {} # (index, total) -> # of ways
        def backtrack(i, total):
            # base case
            if i == len(nums):
                return 1 if total == target else 0
            # cache
            if (i, total) in dp:
                return dp[(i, total)]
            
            # dp of index 0, starting with total 0 has 5 total unique permutations
            dp[(i, total)] = (backtrack(i + 1, total + nums[i]) +
                              backtrack(i + 1, total - nums[i]))
            # print(dp)
            return dp[(i, total)]
        return backtrack(0, 0)

sol = Solution()
output = sol.findTargetSumWays([1,1,1,1,1], 3)
print(output)
