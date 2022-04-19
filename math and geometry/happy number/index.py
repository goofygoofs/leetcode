"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

 

Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
Example 2:

Input: n = 2
Output: false
 

Constraints:

1 <= n <= 231 - 1
"""

"""
take each indiviual digits, square it, and add it together
keep doing this until you get 1
or... endless loop?
question - endless loop -what causes this?

2 => 4 => 16
1 + 36 => 37
9 + 49 => 56
25 + 36 => 61
36 + 1 => 37

set => any number we've seen => add total to this
if we reach that number, it's a loop

func goes loops through each digit and square it and add it => add to set
use that for next iteration

O(l) l is length of digits
O(l) for the set

can create another function for sumOfSquares

can mod it by 10 for the last digit
can divide by 10 to remove last digit (double divide to floor it so we have no decimals)
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        currNum = n
        
        def sumOfSquares(n: int) -> int:
            output = 0
            # mod will give last digit
            while n:
                digit = n % 10
                output += digit * digit
                n = n // 10
            return output

        while currNum not in seen:
            seen.add(currNum)
            if currNum == 1:
                return True

            currNum = sumOfSquares(currNum)
        return False
    


sol = Solution()
output = sol.isHappy(19)
print(output)
