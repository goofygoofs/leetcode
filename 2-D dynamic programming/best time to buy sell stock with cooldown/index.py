'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Example 1:

Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]
Example 2:

Input: prices = [1]
Output: 0
 

Constraints:

1 <= prices.length <= 5000
0 <= prices[i] <= 1000
'''

'''
base case is if len(prices) < 2, return 0

[1,2,3,0,2]
|
buy, sell, do nothing

day 1
do nothing - 0 
buy - 1

day 2
do nothing - 0
buy - 2
sell - 1

        1   2   3   0   2
buy     1   2   3   0   2        
sell        1   2   2   3
nothing
output = 0
L R
[1,2,3,0,2]
 0 
 
 if nums[r] > nums[l]:
     take profit
Q: how do we know when to take profit and how do wse keep track if we don't?
'''

'''
can't have multiple shares, have buy more than 1 share. 

[1,2,3,0,2]
            0
        buy|            |cooldown
          -1            0
     sell| |cooldown  buy|   |cooldown
        +1  -1
        |cooldown
    buy|(0+1)   |cooldown
    |           +1
    +1
    .....
O(2^n)
use caching to O(n) time
(i int, buy/sell bool)
(n max, 2 max) => O(n)



'''

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # state: buying or selling?
        #  if buy -> i + 1
        #  if sell -> i + 2 (for cooldown day)

        # cache
        dp = {} # key=(i, buying) val=max_profit
        
        # buying bool is "can i buy?" False if i already bought because
        # can't buy more than 1 stock
        def dfs(i, buying):
            # print('i', i, 'buying', buying, 'dp', dp)
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]
            
            cooldown = dfs(i + 1, buying) # always have choice of cooldown
            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                dp[(i, buying)] = max(buy, cooldown)
            else:
                sell = dfs(i + 2, not buying) + prices[i]
                dp[(i, buying)] = max(sell, cooldown)
            # print('final i', i, 'buying', buying, 'dp', dp)
            # returns maximum value profit at index i (starting index will return max profit for entire array)
            return dp[(i, buying)]
        
        return dfs(0, True)


sol = Solution()
output = sol.maxProfit([1,2,3,0,2])
print(output)
