'''
Reverse bits of a given 32 bits unsigned integer.

Note:

Note that in some languages, such as Java, there is no unsigned integer type. In this case, both input and output will be given as a signed integer type. They should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 2 above, the input represents the signed integer -3 and the output represents the signed integer -1073741825.
 

Example 1:

Input: n = 00000010100101000001111010011100
Output:    964176192 (00111001011110000010100101000000)
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.
Example 2:

Input: n = 11111111111111111111111111111101
Output:   3221225471 (10111111111111111111111111111111)
Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is 10111111111111111111111111111111.
 

Constraints:

The input must be a binary string of length 32
 

Follow up: If this function is called many times, how would you optimize it?

'''

'''
reverse the binary integer and return the binary representation of that

reverse all teh bits of this integer
let's suppose we have an output where we have 32 bits in the output
and intiallly we set all of these to zeros
we want to go bit by bit from the input and if it's a 0 or a 1 and put it 
into the output starting from the left side
we do this because they specifically tell us this is a 32-bit integer
question is how can we actually do these operations for example
how can we go bit by bit get the first bit... until the end and get each bit
one way in binary is to take the right bit and &(and) it by 1
if we get 0 & 1 = 0
1 & 1 = 1
now how do we &1 each bit?
we keep shifting it by 1 to the left
how can we shift 1 to the left?
that's another binary operation
so for example if we have something like 01
and then we do the shift operation to the left this is a bit shift operation if we shift it to the left
all that does is it shifts all of the bits to the left by one
and replaces the one spot with a zero
01 << 1 => 10 (shift 1 to the left and replace the 1 with a zero)
and the rest will be zero, because if we & 0 with the rest of the 32 bits, &0 will give 0
how are we gonna put it in the output?
if we had a 1, we will shift it to the left by 31 because that's going to be
the spot all the way to the left
we want to logic OR | it. to find what we want to replace it with
0 | 1 = 1
0 | 0 = 0
O(1) time becauise only 32 loops
O(1) space
'''
from collections import deque
class Solution:
    def reverseBits(self, n: int) -> int:
        # res initialized as 0 meaning all 32 bits of it going to be 0
        res = 0

        for i in range(32):
            # get the i'th bit
            # if we & it by 1 every time we are goingg to only get the first bit
            # so we can take n shift it to the right by i
            bit = (n >> i) & 1
            # then we want to logic OR | it with the output to put that bit in the output
            # but we want it in reverse order we want to start at the largest bit then work our way down
            # we can shift our bit over to the left by 31 - i
            # the rest gets ignore which is why we can update res as below, it will only
            # affect the 31-i'th position
            res = res | (bit << (31 - i))
        return res