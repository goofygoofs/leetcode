'''
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

 

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
 

Constraints:

1 <= digits.length <= 100
0 <= digits[i] <= 9
digits does not contain any leading 0's.
'''

'''
array problem
obvious -> loop through and "" + str(int)
int(str) + 1 => array
O(n) time
O(n) space - str buildup

array - properties 
only time make array bigger is if we have a 9 specifically 9 in the last digits, this can also affect if there's 
subsequent 9's before that 9

besides the 9
we can alter the original array last digit by +1, and return it

what if it's a 9?
1) a bigger array by 1 digit ie) 9=>10 => O(n) [1] + original array
2) 89 => 90. while loop that we reach a digit not 9, just increment by 1, if it's a 9, change it to a 0

'''

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        pointer = len(digits) - 1

        digits[pointer] += 1
        extraDigit = False

        while digits[pointer] == 10:
            digits[pointer] = 0
            if pointer == 0 and digits[pointer] == 0:
                extraDigit = True
            pointer -= 1
            if pointer >= 0:
                digits[pointer] += 1

        if extraDigit:
            return [1] + digits
        return digits
             