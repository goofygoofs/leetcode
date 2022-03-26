'''
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.
 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1
 

Follow up: Could you solve it without converting the integer to a string? *
'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        '''
        # string method first O(n)
        strInput = str(x)
        reverseStrInput = strInput[::-1]
        return strInput == reverseStrInput
        # str() is O(n) time
        # reverse the string is O(n) time
        # O(n) space
        '''
        # without string - stack
        # length of the integer
        # 4444 - yes 
        # 333 - yes 
        # -3 = no
        # 10 = no
        '''
        mod
        1) compare first and last digit and repeat process
        2) we need the order of the number. so 121 is on the order of 100
        3)w
        '''
        divisor = 1 # 1=>10 ~~~ 100 ~~~ 1=>10
        # find order of input x
        while (x / divisor >= 10): # 121/1 => 121/10 = 12.1 => 1.21 ~~~ didn't go in because negative ~~~ 10/1 
            divisor *= 10
        
        while (x != 0): #121 ... 2 ~~~ -121 ~~~ 10
            leading = x // divisor #121//100 =>1.21=>1.00 ... 2//1 => 2 ~~~ -121 // 1 => -121 ~~~ 10 // 10 => 1
            trailing = x % 10 #121 %10 =>12.1=> 1.00  ... 2 % 10 => 2 ~~~ -121 % 10 => -13 with 9 remainder => 9 ~~~ 10 % 10 => 0

            # if first and last digit are not the same return false
            if (leading != trailing):
                return False


            # removing the leading and trailing digit from the number
            x = (x % divisor) // 10 # 121%100=> 21 // 10 => 2.1 => 2 ... 2 % 1 => 0

            # reducing divisor by a factor of 2 as 2 digits are dropped
            divisor = divisor / 100 # 1

        

        return True
        # O(log(n)) time while loop divide input by 10 for each iteration
        # space O(1)



solution = Solution()

output = solution.isPalindrome(121)
print(output)

output = solution.isPalindrome(-121)
print(output)

output = solution.isPalindrome(10)
print(output)