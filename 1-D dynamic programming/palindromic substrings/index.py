'''
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

 

Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 

Constraints:

1 <= s.length <= 1000
s consists of lowercase English letters.
'''

'''
a and a at diff index do count
we expand out from the middle character => O(n^2)
check even and odd edge case
set() stores (pal substring, startingIndex) => store duplicates at diff index

time - O(n^2)
space - O(n) 

update: remove set and just update count for O(1) space
'''

# O(1) space
class Solution:
    def countSubstrings(self, s: str) -> int:
        self.count = 0
        def helper(i: int) -> None: # find all palindromes at given index expanded outwards. i is middle of palindrome
            l = i-1
            r = i+1
            while l >=0 and r < len(s) and s[l] == s[r]:
                self.count += 1
                l-=1
                r+=1
            # even case
            l = i
            r = i+1
            while l >=0 and r < len(s) and s[l] == s[r]:
                self.count += 1
                l-=1
                r+=1
        for i in range(len(s)):
            self.count +=1
            helper(i)
        return self.count

