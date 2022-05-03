'''
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
 

Constraints:

1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
'''

'''
build a Trie
if we reach trie.isWord = True, then dfs() into there
dfs(s[0])
leet ->T
code ->
cat(s)->
 
'''

'''
brute force? check first char, then first 2 chars ... until we find first matching word in our wordDict
Q: now what do we do when we find a word?
clearly we have a sub problem we found a matching word for this portion but now we want to know can we break up the rest of this string
with words from our dictionary? this is our subproblem
O(n^2) for trying every possible prefix
we can also check every word in our dictionary if it matches for example the first word is "leet"
it matchs so there's only 4 chars left and do the same thing
does leet match "code"? no. does "code" match "code"? yes
instead of check every possible prefix, we check every possible prefix
this is O(n * m) n is potentially every single character of s * m (which is number of words in wordDict)
they say max size of worddict is less than size of s, so this is more efficient
s = "neetcode" wordDict = ["neet", "leet", "code"]
i = 0
|       |       |
neet    leet    code
|
i=4
|       |       |
neet    leet    code
                | i = 8
                return True

example for cache
i = 5 
dp[5] = False
so we don't have to do it again

for dp solution

dp[8] = True (end of string)
dp[7,6,5] = False
dp[4] = True (code)
dp[3,2,1] = False
dp[0] = True (neet) =>  dp[0 + len(dp4) ] = True

the True from the last position (len + 1) carries our True over
we just update dp[i] = dp[i+len(w)]
'''

from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1) # +1 for our base case
        dp[len(s)] = True # last positioin is false
        
        for i in range(len(s)-1, -1, -1):
            for w in wordDict:
                # if starting at position i, the string s has enough characters
                # for w to be compared to it
                # if the substring is exactly equal to the word in wordDict
                # print(i + len(w))
                if s[i:i+len(w)] == w:
                    dp[i] = dp[i + len(w)]
                # if we found our word, we cant stop looking at other words in wordDict
                if dp[i]:
                    break
        return dp[0]

