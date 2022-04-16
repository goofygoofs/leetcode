'''
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

 

Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
 

Constraints:

0 <= n <= 105
 

Follow up:

It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?
Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?
'''

'''
O - n , n = 2
0, 1, 2
what is the number of 1's in the binary representation of each of these integer?
[0, 1, 1]
brute force is nlgn. 3%2=1 then keep doing doing that until we get total # of 1's. when we get to 0 after /2 or shifting over, we stop. 
doing this n times it will be nlogn

we can do this in O(n) times
0 - 0000 - 0
1 - 0001 - 1
2 - 0010 - 1
3 - 0011 - 2
below is just repeat of above
4 - 0100 - 1 + dp[0] => 1 + dp[n-4] => this is a dynamic programming problem. take how many 1's are in the 4th previous position before it
5 - 0101 - 1 + dp[n-4] => 2
6 - 0110 - 1 + dp[n-4] => 2
7 - 0111 - 1 + dp[n-4] => 3

8 - 1000 - 1 + dp[n-8] => 1
this is the equation 1 + dp[n-int] where int is the offset
and the offset is going to be the most significant bit that we have reached so far
and what are the most significant bits well
the first one is going to be 1,2,4,8,16...
basically that double each time or power of 2^n
how do you know if you've reached a new power of 2?
well let's say the current power of 2 is 2, let's say we multiply it by two
if we get to 4, we ask does 2x2 = 4? yes
when we get to 7, we ask does 4x2=7? no but it does at 8

time - O(n) where n is 0->n+1
space - O(n) for dp aray

'''

from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        offset = 1

        for i in range(1, n + 1):
            # first we check if we can double our offset (which does at every power of 2)
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        
        return dp
