'''
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
'''

'''
s2 contains a permutation of s1?
letter, index are important
index can be reversed, ie. "ab" and "ba" but "boa" won't work

put all characters of s1 into a dictionaryy
copy dictionary
loop through s2 and find out where it starts containing letters from s1 and minus 1, until length of copied dicionary is 0. get the start and end indexes and make new string out of it


check if length is equal
create another function to find out if permutation exists
actually permutation, the ordering doesn't matter. so just the dictionary portion matters


so... that means we have to make sure no other letters in substring of s2. and also careful of duplicates. 
if there's duplicates we can remove the firstmost index of found character and see if it affects sustring

"aab" "zzeaaab"
"aaaaa" "sadfw3efdafds"

what if there is only 1 char in dict?

Time compliexity is O(n) for creating dictionary and looping through s2
well it is O(m+n)
space is O(m) for s1 dictionary and copying it
'''

'''
2 solutions
O(26 * n)
O(n)

we're given 2 strings s1 and s2 and all we want to do is return True if s2 contains a permutation of s1
and false otherwise. s1 is the target string. permutation of this string inside of s2
what does permutation mean? in here there is a substring of s1 in a different order.
ab counts as a permutation of ab. is there a substring of the exact same size.
we are looking for a window the same size as this in a different window.
same thing as looking for an anagram.
use the typical sliding window technique.
look at every window in s2 same size as s1
length 2 in this case. comparing exact character would be O(m*n) m is size of s1 and n the size s2
if we use hashmap, at most will be O(26*n)
we will have 2 hashmap, one for s1, and s2
everytime we create a window, we just remove one character to the left, and add one to the right

a slightly better way is O(n)
still have 2 hash maps
s1 = "abc" s2"baxyzabc"
we fill our s1 and s2 hashmaps and fill it up to the window and move it each time
we will have 1 more variable called matches, initially set to 0
basically shortcut so we dont have to compare entire hashmap which at worse will be a 26 operation (a->z)
matches will maintain total number of equal characters in each of these hashmaps
we want to know the number of matches initially, it can be 0 to 26
if the first window was "abc", it will be 26 matches for the abc character there is 1 and rest of 23 characters is 0
so therefore they have 26 matches and we can do that with a single variable without looking through the hashmap each time
it's a single O(26) + O(n) operation
so comparing first window "abc" and "bax" they match everything but c and x
so intially they have 24 matches
when we shift it, we remove a character from the hashmap. does it affect the match?
we decrement as we shift windows and there will be a mismatch, so matches count will go to 23->22->21->20
the remaining 3 spots we will add the a, b, c character and our matches will be 26
when we hit 26 matches, we will stop the algorithm and return true
O(26 + n) time complexity
O(1) space since only 26 characters in 2 hashmaps
if len(s1) > len(s2) return false immediately
for sliding window we are going to initialize a left pointer to be at the beginning
we are going to start at the length of s1 because this will start us at the next character 
we left off at right and this range is actually non-inclusive so we stopped before we reach this index
only need to initialize with length of s1 for s2dict
what if same character? do prev, then curr next
'''
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1dict = {}
        s2dict = {}
        matches = 0
        alphabet = "abcdefghijklmnopqrstuvwxyz"

        for char in alphabet:
            s1dict[char] = 0
            s2dict[char] = 0

        for i in range(len(s1)):
            s1char = s1[i]
            s2char = s2[i]
            s1dict[s1char] += 1
            s2dict[s2char] += 1
            

        for char in alphabet:
            if s1dict[char] == s2dict[char]:
                matches += 1
        if matches == 26:
            return True
        # sliding window
        # need a leftpointer. actually do not need left pointer
        # leftPointer = 0
        # print('s1dict', s1dict)
        for i in range(len(s1), len(s2)):
            previousChar = s2[i - len(s1)]
            currChar = s2[i]
            # print('s2dict', s2dict)

            s2dict[previousChar] -= 1 #previous and current seperately, because what if same characters? will mess up match
            if s1dict[previousChar] == s2dict[previousChar]:
                matches += 1
            elif s1dict[previousChar] == s2dict[previousChar] + 1: # if the same before, only then subtract
                matches -= 1
            
            s2dict[currChar] += 1 #previous and current seperately, because what if same characters? will mess up match
            if s1dict[currChar] == s2dict[currChar]:
                # print('currChar', currChar)
                matches += 1
            elif s1dict[currChar] == s2dict[currChar] - 1: #only if it was the same beofre, only then subtract
                matches -= 1
            # print('matches', matches)
            if matches == 26:
                return True
        return False

# sol = Solution()

# output = sol.checkInclusion(s1 = "trinitrophenylmethylnitramine", s2 = "dinitrophenylhydrazinetrinitrophenylmethylnitramine")
# print(output)

# output = sol.checkInclusion(s1 = "abc", s2 = "bbbca")
# print(output)

# output = sol.checkInclusion(s1 = "ab", s2 = "eidbaooo")
# print(output)

# output = sol.checkInclusion(s1 = "ab", s2 = "eidboaoo")
# print(output)
