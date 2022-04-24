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

from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1
        output = set()

        def dfs(i: int, amountLeft: int, coinUsed: List[int]) -> None:
            if amountLeft == 0:
                coinUsed.sort()
                # change to Tuple because we cant add list to set because they are mutable
                # tuples are unmmutable
                output.add(tuple(coinUsed))
                return
            for j in range(i, len(coins)): # not i+1 because we can re-use the same coin
                if amountLeft >= coins[j]:
                    copyCoinUsed = coinUsed.copy() # new array so it doesn't interfere with other dfs'
                    copyCoinUsed.append(coins[j])
                    dfs(j, amountLeft - coins[j], copyCoinUsed)

        
        for i in range(len(coins)):
            dfs(i, amount - coins[i], [coins[i]])
        return len(output)