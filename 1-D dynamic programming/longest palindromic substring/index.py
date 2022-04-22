'''
Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
'''

'''
palindrome? 
spelled same backward as forward
bab
pointers
left, right
zbabad
l    r
Q: how do we know which way to increment?
How do we know the start and end of the palindrome?
bab
aba

brute force

dict {
    a: [leftmost, rightmost indices]
    .....
    z
}

heap (distance, "char", left, right)

'''

'''
palindromic substring - if wrote in reverse order, it's the exact same string
we can start at the beginning O(n^3)or...  
start at the middle of the palindrome and work our way outwards
consider each character as the middle => O(n^2)

even and odd palindrome - consider this edge case

time - O(n^2)
space - O(n) for output str
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        for i in range(len(s)):
            # odd len palindromes
            l, r = i, i # center position
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1
            # even length
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1
        
        return res