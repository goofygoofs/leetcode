'''
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
 

Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104
'''

'''
return -1 if not possible
integer array of coins
amount represent total amount of money
return fewest number of coins needed to make that amount
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

11%5 => 1 check if 1 in coins?
11/5 => 2

while 

for 
    go reversed
'''

'''
greedy, start with the right most number and keep going down
[1,3,4,5] amount = 7
5 + 1 + 1 = 7 (3 coins WRONG answer because we can use 3+4)
so we can't use Greedy

DFS backtracking?
            7
    |1    |3    |4   |5
     6     4    3    2
                    |1  |3  |4  |5
                    1   -1  -2  -3
                    | |||
                    0 (negatives) 
                    (minCoin = 3)
we do it for all the other numbers and can see some subproblems repeat, so we don't have to do those if we cache it
this is top down
but we can do DP-bottom-up
so we start with what is dp[0]->0
dp[1]->1 (coin)
dp[2]->1 + dp[1]
dp[3]->1 
...
dp[7] = 1(1 coin)+DP[6] => 3
      = 1(3 coin)+DP[4] => 2
      = 1(4 coin)+DP[3] => 2
      = 1(5 coin)+DP[2] => 1+2=3

time - O(amount * len(coins))
space - O(amount) for array
'''

from typing import List, Tuple


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # amount + 1 because we are going from 0...amount(7)
        dp = [float('inf')] * (amount + 1)
        # base case, dp[0] = 0 (coins)
        dp[0] = 0
        
        # going bottom up
        for index in range(1, amount + 1):
            for c in coins:
                if index - c >= 0:
                    dp[index] = min(dp[index], 1 + dp[index - c])
                    # print(dp)
        return dp[amount] if dp[amount] != float('inf') else - 1

# sol = Solution()
# output = sol.coinChange([1,3,4,5], 7)
# print(output)