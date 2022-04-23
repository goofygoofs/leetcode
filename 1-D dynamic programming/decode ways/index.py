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


class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        output = 1
        for i in range(len(s)):            
            if i == 0: # skip first
                continue
            if s[i] == "0" and s[i-1] not in ("1", "2"):
                return 0
            if s[i] != "0" and s[i-1] in ("1"):
                output += 1
            if s[i] not in ("0", "7", "8", "9") and s[i-1] in ("2"):
                output += 1
        return output

sol = Solution()
output = sol.numDecodings("12")
print(output)