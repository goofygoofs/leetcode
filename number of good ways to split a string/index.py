'''
You are given a string s.

A split is called good if you can split s into two non-empty strings sleft and sright where their concatenation is equal to s (i.e., sleft + sright = s) 
and the number of distinct letters in sleft and sright is the same.

Return the number of good splits you can make in s.

 

Example 1:

Input: s = "aacaba"
Output: 2
Explanation: There are 5 ways to split "aacaba" and 2 of them are good. 
("a", "acaba") Left string and right string contains 1 and 3 different letters respectively.
("aa", "caba") Left string and right string contains 1 and 3 different letters respectively.
("aac", "aba") Left string and right string contains 2 and 2 different letters respectively (good split).
("aaca", "ba") Left string and right string contains 2 and 2 different letters respectively (good split).
("aacab", "a") Left string and right string contains 3 and 1 different letters respectively.
Example 2:

Input: s = "abcd"
Output: 1
Explanation: Split the string as follows ("ab", "cd").
 

Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters.
'''

'''
26 letters in alphabet
set / dict to find unique
 
 go through it n times, and at each spot, either return True if good split or just add one as we are traversing through n

set for left side, dict for right side, so we don't have to keep looping 
'''
class Solution:
    def numSplits(self, s: str) -> int:
        goodSplits = 0
        leftSet = set()
        rightDict = dict()
        # populate rightDict
        for char in s:
            if char not in rightDict:
                rightDict[char] = 1
            else:
                rightDict[char] += 1
        
        uniqueLeft = 0
        uniqueRight = len(rightDict) 
        for char in s:
            if char not in leftSet:
                leftSet.add(char)
                uniqueLeft += 1
            rightDict[char] -= 1
            if rightDict[char] == 0:
                del rightDict[char]
                uniqueRight -= 1
            # see if good split
            if uniqueLeft == uniqueRight:
                goodSplits += 1
        
        return goodSplits
"""
O(n) time complexity
O(n) space
"""

sol = Solution()

output = sol.numSplits("aacaba")
print(output)

output = sol.numSplits("abcde")
print(output)