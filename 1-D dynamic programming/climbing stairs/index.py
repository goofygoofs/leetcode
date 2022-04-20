'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45
'''

'''
3
if it's the same number, order does not matter
different numbers, order matters
1 + 1 + 1
1 + 2
2 + 1

1 - 1
2 - 2

4
2(3) + 2(3) = 6
1 + 1 + 1 + 1
2 + 2
1 + 2 + 1
1 + 1 + 2
2 + 1 + 1

_ _ _ _ _ _  _
1 2 3 5 8 13 21

pattern we get the prev + prev.prev amount of ways will give us current
but question is why?
NOT SURE 
top->bottom => because we need the previous 2 to compute the next one
store the last 2 we've seen

time - O(0->n) range
space - O(1)

reasoning ?
'''

'''

'''

class Solution:
    def climbStairs(self, n: int) -> int:
        prev = 1
        prevPrev = 0
        index = 0

        if n == 1:
            return 1

        while index < n:
            index += 1
            tmp = prevPrev
            prevPrev = prev
            prev += tmp
        return prev

