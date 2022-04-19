'''
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

 

Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
 

Constraints:

-100.0 < x < 100.0
-231 <= n <= 231-1
-104 <= xn <= 104
'''

'''
2^10
= 2*2*2...(10x)
2^-10
= 2*2*2...(10x) => 1/(2*2*2...)

O(n) time where n is the exponent

is there a quicker way? (divide and conquer)
2^10 => 2^5 * 2^5? = 2^10

2^5 => 2* 2^2 * 2^2
2^2 = 2^1 * 2^1

divide and conquer
time - O(logn)
base case
if n = 0, return 1
if x = 0 , return 0
'''

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x: float, n: float) -> float:
            if x == 0:
                return 0
            if n == 0:
                return 1
            # n = 5 => 2 => x * x^2 * x^2
            res = helper(x, n // 2)
            res = res * res
            if n % 2 == 0:
                return res
            return x * res

        res = helper(x, abs(n))
        return res if n >=0 else 1 / res