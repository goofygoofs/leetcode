'''
Given two integers a and b, return the sum of the two integers without using the operators + and -.

 

Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = 2, b = 3
Output: 5
 

Constraints:

-1000 <= a, b <= 1000
'''

'''
01 => 1
10 => 2
---
11 => 3
if we had a 1 and a 0, adding these together gives us 1
what  operation can we do with using the + operation?
01
01
--- 
10
for 1 and 1 it will be 0 and carry over the 1 to the left
if one of these is a 1 digit, then it will be a 1. if both 0 or 1's, will be 0.
XOR 
if it's the same, will give 0
if it's 1 and 0, will give 1
but how do we do the 1 carry? for 1+1?
how do we know we have 1 and 1?
we can use the & AND operator and shift it over by 1
(a & b) << 1
we don't have to do it one by one, we can do it for the entire 32 bit integer a and b
1001 => 9
1011 => 11
-----
a ^ b       => 0010 . but we didn't shift over the 1+1. XOR adds these numbers but doesn't do carry
a & b << 1  => 10010 
------- Do XOR and & shift over left by 1 again
       0010
      10010
      ------
^     10000
&<<1  00100
-----------
^     10100 => 20
we don't have a carry in this case, we are done
O(n) time or O(1) time depending on the XOR & shift over by 1

but in python, integers can exceed 32 bits. so we need a mask variable of 32 bits of 1's 
so we don't overflow
also we need ~(a ^ mask to juggle from the positive number to the negative complement)
'''

class Solution:
    def getSum(self, a: int, b: int) -> int:

        mask = 0b11111111111111111111111111111111       
        MAX =  0b01111111111111111111111111111111
        
        if b == 0:
            return a if a <= MAX else ~(a ^ mask)
        
        return self.getSum(
            (a ^ b) & mask,
            ((a & b) << 1) & mask
        )