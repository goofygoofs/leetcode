"""
A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The test cases are generated so that the answer fits in a 32-bit integer.

 

Example 1:

Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
Example 3:

Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").
 

Constraints:

1 <= s.length <= 100
s contains only digits and may contain leading zero(s).
"""

"""
the trick is 2 digit number, like J - 10
06 is NOT F. F is 6.
we have to find out how many ways it can be decoded
12 => 12 or 1 and 2
L or AB

for 2 digits, the first digit can be 1 or 2
if it's a 0, it can only be decoded 1 way
there's no character for 0

A 1
B 2
C 3
D 4
E 5
F 6
G 7
H 8
I 9
J 10
K 11
L 12
M 13
N 14
O 15
P 16
Q 17
R 18
S 19
T 20
U 21
V 22
W 23
X 24
Y 25
Z 26

10 1234
11 23 
J A B D
J A W
J L C D

if it's 1 or 2 we gonna check the next index if exist. if it's any
digits besides 0, we gonna add 1
while iterating we don't add 0's
"""

"""
how many different ways can we take string of integers and decode it to characters
we are given map of A->1...Z->26
"12" = 1(A) and 2(B) or 12(L)
problem comes from double digits like 10
2 different decisions with 10
there's a few different edge cases like "06"
"0" is not in our input
any string starting with "0" is invalid
    1   2   1
any integer by itself except 0 can be taken
|       |
1       12
| |     
2 21
|
1
count: 3

first digit 1 , we can take [0-9]
first digit 2, we can take [0-6]
if we take 2 decisions at every node, it would be 2^n
how can we do better?
if we take 1 by itself and consider this is just going to be one way to decode it
then we're asking how many different ways can we decode the remaining of the string 
the sub problem over here we're asking
how many different ways can we decode 21 when we take the first two characters 12 then we're asking
how many different ways can we decode the string 1. that's how the sub problem works
the sub problem is just going to be some portion of the string you know 
to solve this problem how many ways can we decode this we have to solve the sub problem how many ways
can we decode everything excep the beginning
so basically you know how many different ways can we cache it 
we gonna have an index i and dimension of our cache is going to be n
and that's going to be time complexity
O(n) time
O(n) space for cache

can be solved without a cache so O(1) memory
to compute we only need to look at the 2 values that come after it
dp[i] = dp[i+1] + dp[i+2]
we don't need a full array just 2 values

O(n) memory cache
if i in dp cache, return dp[i]
set res = dfs(i+1)
if in bounds for 1 [0-9] or 2[0-6]
    res += dfs(i+2)
dp[i] = res
return res
"""

class Solution:
    def numDecodings(self, s: str) -> int:
        # O(n) time and space solution
        # initialize cache. base case to return 1 for entire string
        dp = {len(s): 1}
        def dfs(i: int) -> None:
            print('i', i)
            if i in dp:
                # already been cached or i is in the last position in the string
                return dp[i]
            # if not end of str we gotta check what character it is
            if s[i] == "0":
                return 0
            # between 1 - 9
            res = dfs(i + 1)
            print(dp, "i", i)
            if (i + 1 < len(s) and (s[i] == "1" \
                or s[i] == "2" and s[i+1] in "0123456")): # if starts with "1" we know we can make a double digit value
                # if good value for 2 in [0-6]
                # if we do have a second character after this one
                res += dfs(i + 2)
            dp[i] = res
            return res
        return dfs(0)

sol = Solution()
output = sol.numDecodings("121")
print(output)