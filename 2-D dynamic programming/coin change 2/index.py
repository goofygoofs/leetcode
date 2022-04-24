'''
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer.

 

Example 1:

Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
Example 3:

Input: amount = 10, coins = [10]
Output: 1
 

Constraints:

1 <= coins.length <= 300
1 <= coins[i] <= 5000
All the values of coins are unique.
0 <= amount <= 5000
'''

'''
dfs if total - coins[i] >= 0
2 + 2 + 1 vs 2 + 1 + 2? or even 2< + ->2 + 1
sort answer before adding to set?

O(n^2)
O(n) stack 
'''

'''
unbounded knapsack problem
can't change order and call it a different combination
c^n => c is # of coins and n is amount we want to sum up to
m * n is best time complexity we can do

            0
        |       |   |
        1       2   5
        | | |    (how about this path can't chose 1's or previous values) (unique combinations)
        2 1 1
        | | |
        2 1 1
          | |
          1 1
          | |
          1 2
          |
          1
we are going to maintain a pointer so we are not not allowed to choose an index less than it
memoization
m^n - m is # of coins we have and n is the total amount (height of the tree)
dfs(i, amount) if amount > 5(target), we stop
m * n = total possible number of ways is m*n called
if we cache, we don't have to repeat same work
time O(m*n)
space O(m*n)

optimized dp soln 
space O(n) 

dp soln is more optimized than recursive memoization sooln
                amount
            5   4   3   2   1   0 (how many ways can we sum up to 0 with coins [1,2,5] is 1 way (0 coins))
coin    1                   1   1
        2                   0   1
        5                   0   1    
gotta have entire 2d grid in memory 

O(n) memory

                amount
            5   4   3   2   1   0 
coin    1   4   3   2   2   1   1        (add right and down to get spot)                  
        2   1   1   0   1   0   1        (as we go up we can look 1 down to move up the amount of possible ways)           
        5   1   0   0   0   0   1
when we look down we don't need to look mujltiple spots down, that's the key to O(n) memory
we still may need to look mujltiple spots to the right
''' 

from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # O(n) memory
        # O(n*m) time
        dp = [0] * (amount + 1)
        dp[0] = 1
        # bottom up dp
        for i in range(len(coins)-1,-1,-1): # iterating through coins backwards
            # print('dp', dp)
            nextDP = [0] * (amount + 1)
            nextDP[0] = 1

            for a in range(1, amount + 1): # iterating through 1->amount (since we've calculated for 0 already)
                nextDP[a] = dp[a]
                if a - coins[i] >= 0: # only when the amountLeft can fit into that coin
                    # print('i', i, 'a', a, 'nextdp[a]', nextDP[a], 'coins[i]', coins[i], 'nextDP[a-coins[i]]', nextDP[a-coins[i]])
                    nextDP[a] += nextDP[a - coins[i]] # take the bottom number + all the way to the right// or right next it it depedning on the coin
            # print('nextDP', nextDP)
            dp = nextDP
        return dp[amount]

sol = Solution()
output = sol.change(5, [1,2,5])