'''
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

 

Example 1:

Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.
Example 2:

Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.
 

Constraints:

2 <= cost.length <= 1000
0 <= cost[i] <= 999
'''

'''
start at index 0 or 1 in array 
[10, 15, 20]
if i start at 15, i climb 2 steps to reach the top
if i start at 10, I climb 1 or 2 steps, it will be higher than 15

[1,100,1,1,1,100,1,1,100,1]
 -     -   -     - -     - -

 [6, 105, 5, 5, 4, 102, 3, 2, 100, 1] 
min (index 0, 1)
initialize array of len(cost) with 0's
what is the min cost to get to this step?

should we get reversed or forward?
let's go reverse
pointer at the end

O(n) time where n is length of cost
O(n) space for the array
'''

from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # base case
        if len(cost) == 2:
            return min(cost)
        
        # 3 or more, we can use our function
        dp = [0] * len(cost)
        # setting the 2 initial from the back
        dp[len(cost)-1], dp[len(cost)-2] = cost[len(cost)-1], cost[len(cost)-2]
        for i in range(len(cost)-3, -1, -1):
            dp[i] = min(cost[i] + dp[i+1], cost[i] + dp[i+2])
        return min(dp[0], dp[1])
        