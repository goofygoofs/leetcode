'''
Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

Note:

Note that in some languages, such as Java, there is no unsigned integer type. In this case, the input will be given as a signed integer type. It should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3, the input represents the signed integer. -3.
 

Example 1:

Input: n = 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
Example 2:

Input: n = 00000000000000000000000010000000
Output: 1
Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.
Example 3:

Input: n = 11111111111111111111111111111101
Output: 31
Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.
 

Constraints:

The input must be a binary string of length 32.
 

Follow up: If this function is called many times, how would you optimize it?
'''

'''
take a look at this number and return the number of 1's it has
2 solutions
count manually bit by bit.
look at the bit on the right side. logic and operation it's gonna be a 0 or 1
for every bit. it's gonna be 0 for every bit except for the rightmost one which can be 0 or 1
it'll be 1 if the bit in the input integer is 1 then we'll get a 1 in the output if it's a 0

we can mod it by % 2 and we'll get a 1 if the remainder is 1 or a 0 if the remainder is 0 (the last integer)
so we have a way to look at the last bit and see if it's 1 or 0.
how do we check the other bits?
we can take all the rest of the bits and then shift them to the right by one
shift every bit to the right by one
dividing by /2 will usually shift all the bits to the right by one but usually the bit shift operation
is a little bit more efficient on your cpu so that's what we're gonna prefer
we're gonna take the bits and shift over the right by 1 then mod % 2 to find out if 0 or 1
once we have the last 1 and shift it to the right, we only gonna have a 0, so that's how we know we're done

guaranteed that every input is going to be a 32-bit integer so the while loop we had is going to run 32 times
so time complexity is 32 so constant
time complexity O(32) => O(1)
space O(1)
downside to our solution is that is looks at every bit even if it isn't 1
wouldn't it be convenient if our algo only runs when there's a 1?
'''

class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            # %2 will return 0 if 0 and 1 if 1 for the rightmost bit
            res += n % 2
            # shift bit to the right by 1
            n = n >> 1
        return res

        # 2nd solution. runs only for how many 1's there is
        # why does this work?
        # we subtract 1 it removes the last 1 bit and the & and will zero out everything but remaining 1's
        # we then increment for each time this happens
        # basically what we're doing is skipping all the 0's in between
        # and we're running this algo as many times as there are 1's in this input integer
        n = n & (n-1)
        res += 1

        res = 0
        while n:
            n &= (n-1)
            res += 1
        return res