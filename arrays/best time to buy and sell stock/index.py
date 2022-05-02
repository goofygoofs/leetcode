'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104
'''

'''
we'll use 2 pointers so we only need to go through the list 1 time O(n)
O(n) time complexity
O(1) space because we use the pointer
1 pointer is on the left and keeps moving down when a lower number is detected
1 pointer is the right and keeps moving if bigger number detected
also we need a variable to keep tax of max. if we go from low to high to lower number, then we get the
difference before we move the lower pointer over
also when we move right pointer from higher -> higher number we take difference to store to max

Input: prices = [10, 50, 1, 40]

check if price > leftValue in addition to price > rightValue when calculating. because you can get a high value but not a higher one so it does not calcualte
    also have to check if right pointer > leftpointer on this
remember to use price when calculating for higher rightValue since rightValue wasn't re-calculated
'''
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP

sol = Solution()

# output = sol.maxProfit([7,1,5,3,6,4])
# print(output)

# output = sol.maxProfit([7,6,4,3,1])
# print(output)

# output = sol.maxProfit([10, 50, 1, 40])
# print(output)
