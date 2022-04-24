'''
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

 

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
 

Constraints:

1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters.
'''

'''
we can create a new substring from the original with deleting some characters without
changing the relative order of the remaining charactreers
match this substring with substring in text 2

a   b   c   d   e
1   0   1   0   1

a   c   z   e
1   1   0   1

Q: how do we know whether we should delete or keep
'''

'''
check the first letter of each text1 and text2. if they match then that's the longest common subsequence 
then we can break it into a sub problem 
1 + subproblem answer
that's what dynamic programming is all about, finding the sub problem
Q: what if the first text is not the same?
then we cannot add 1 and find the longest common subsequence between the remainder of the two strings
we can break it into a different subproblem. we can say it's possible the longest common subsequence could be between
the two strings right 
or between str1 move over by 1 /vice versa
if they match we move diagonally . 
if not match we check the right position and down posiiton
Q what doe sthe right position mean? 
it means we are taking the remaining substring from i and comparing it with substring of j+1 
longest common between string and empty is 0 (bottom and right)
going up means there was no match there. diagonal means there's match (+1)
                j
        a   c   e
    a   3           0
    b       2       0
    c       2       0
i   d           1   0
    e           1   0
        0   0   0   0
bottom up dynamic programming 
as we start from the bottom and work our way up how do we determine what values go into the cell?
we are going to look at the characters and if they match each other
we're gonna say 1 + value that's diagonal right
if characters don't match, take the max of the bottom and right of the cell
time - O(m*n) to go through both string lengths
space - O(m*n) for the dp 2-d array
'''

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) -1 , -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1] # add at diagonal
                else: #characters don't mnatch
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j]) #don't match so we don't add 
        
        return dp[0][0]