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

from typing import List

class Trie:
    def __init__(self) -> None:
        self.children = {}
        self.isWord = False
    
    def add(self, word: str) -> None:
        root = self.children
        for char in word:
            if char not in root:
                root[char] = Trie()
            root = root[char]
        root.isWord = True


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # build Trie
        self.trie = Trie()
        for word in wordDict:
            self.trie.add(word)
        
        def helper(s: str, trie: Trie) -> bool:
            if not s:
                return True
            char = s[0]
            if trie.isWord:
                return helper(s[1:], self.trie[char])
            if char not in trie.children:
                return False
            if helper(s[1:], trie[char]):
                return True

        return helper(s, self.trie)