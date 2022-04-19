'''
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

 

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
 

Constraints:

1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
'''

'''
"2" * "3"
we cannot use int()

dict "0-9": 0-9
for loop through the str?
[1,2,3],join()

O(n) time n len(num1) + len(num2)
O(n) for the dictionary, array

O(1) dict

how do we do multiplication

    123
x   456
--------
    738
   6150 
  49200
--------
  56088
0) for loop within for loop
1) right to left - pointer
2) carry overs
-----------
 1) add right to left - poitner
 2) carry over
'''

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        dict = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9
        }

        for i in range(-1, len(num1), -1):
            pass

print('hello')
for i in range(3, 1,-1):
    print(i)