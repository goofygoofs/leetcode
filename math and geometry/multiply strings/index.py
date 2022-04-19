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

'''
create with an array and convert back to a string afterwards
time - O(m*n) m is len(num1) and n len(num2)
memory - O(m+n) for the array

gotta do it in reverse (9*9)
remove beginning zero's
'''

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1, num2]:
            return "0"
        
        res = [0] * (len(num1) + len(num2))
        num1, num2 = num1[::-1], num2[::-1]
        print(res)

        for i in range(len(num1)):
            for j in range(len(num2)):
                digit = int(num1[i]) * int(num2[j])
                print('i+j', i+j, i, j)
                res[i + j] += digit
                res[i + j + 1] += res[i + j] // 10 # for carry over
                res[i + j] = res[i + j] % 10 # remainder
                print(res)

        # get rid of any leading 0's [5,6,0,8,8,0]
        res, beg = res[::-1], 0
        while beg < len(res) and res[beg] == 0:
            beg += 1
        res = map(str, res[beg:])
        return "".join(res)

sol = Solution()
output = sol.multiply("9", "9")
print(output)