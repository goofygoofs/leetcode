'''
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
 

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
 

Constraints:

0 <= word1.length, word2.length <= 500
word1 and word2 consist of lowercase English letters.
'''

'''
insert - if len(s1) > len(s2)
remove - if len(s1) < len(s2)
edit - in every other situation


O(2N) because we go from the front to the back and iteration from current index to the back

probably use dictionary to keep count of remaining needed characters. if characters out of place, then we need to edit
if valid character still exist and we run into non-needed character without needed character hitting 0, then we can edit

'''
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) == 0 and len(word2) == 0:
            return 0
        word2chars = {}
        for char in word2:
            if char not in word2chars:
                word2chars[char] = 1
            else: # char exists already
                word2chars += 1
        
        minOperations = len(word1)

        for i, char in enumerate(word2):
            word1char = word1[i]
            if word1char == char:
                minOperations -= 1
                continue
            # word[i] != char
            if word1char not in word2chars:
                if len(word1) > len(word2):
                    word2 = self.insert(word2, word1char, i)
                elif len(word1) < len(word2):
                    word2 = self.remove(word2, i)
                else: # equal
                    word2 = self.edit(word2, char, i)
            else: # word1char in word2chars
                word2 = self.remove(word2, i)
        
        print(word2, minOperations)
        # insert rest if length w2 < w1
        if len(word2) < len(word1):
            minOperations += len(word1) - len(word2)
        
        # remove rest if length w2 > w1
        if len(word2) > len(word1):
            minOperations += len(word2) - len(word1)
        
        return minOperations
                


        
    
    def insert(self, word: str, char: str, index: int) -> str: # hose, r, 2 => ho + r + se
        return word[:index] + char + word[index:]
    
    def remove(self, word: str, index: int) -> str: # horse, 2, => hose
        if len(word) == index + 1: # if at last index
            return word[:index]
        else:
            return word[:index] + word[index+1:]
    
    def edit(self, word: str, char: str, index: int) -> str: # hosse, r, 2 => horse
        if len(word) == index + 1:
            return word[:index] + char
        else:
            return word[:index] + char + word[:index+1]

        
sol = Solution()

output = sol.minDistance(word1 = "horse", word2 = "ros")
print(output)