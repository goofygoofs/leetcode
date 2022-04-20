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
at every point we have 2 decisions to make, take 1 step or 2 steps
if we have 2 4's we are repeating the same thing with the decision. ie
2 + 2 = 4 . 3 + 1 = 4
we have 2 decisions each for 4, but they both are the same. 1 or 2 steps.
why are we repeating the same question for these subtrees?
we already know the answer is 2 so we don't need to do the same work again

memoization
dynamic programming
start at the bottom and work the way up


time - O(n) linear

DP = [0,0,0,0,0]
DP = [5,3,2,1,1]
because say at position 2, you can take 1 step or 2 step which lands you at position 3 or position 4
position 3 has 2 possible ways and position 4 is 1 possible way
2 + 1 = 3 possible ways for position 2

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

