'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
'''

'''
if we can re-arrange the characters for anagram then we can you a dictionary
we'll loop through twice for the 2 inputs. create 2 dictionaries and compare to each other

time complexity is O(n)
space is O(n) for the dictionary
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdict = {}
        tdict = {}

        for char in s:
            if char not in sdict:
                sdict[char] = 1
            else:
                sdict[char] += 1
        
        for char in t:
            if char not in tdict:
                tdict[char] = 1
            else:
                tdict[char] += 1

        return sdict == tdict

sol = Solution()

output = sol.isAnagram(s = "anagram", t = "nagaram")
print(output)

output = sol.isAnagram(s = "rat", t = "car")
print(output)