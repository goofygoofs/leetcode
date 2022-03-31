'''
Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

A shift on s consists of moving the leftmost character of s to the rightmost position.

For example, if s = "abcde", then it will be "bcdea" after one shift.
 

Example 1:

Input: s = "abcde", goal = "cdeab"
Output: true
Example 2:

Input: s = "abcde", goal = "abced"
Output: false
 

Constraints:

1 <= s.length, goal.length <= 100
s and goal consist of lowercase English letters
'''
'''
leftmost to rightmost - data structure
i want to go through one time instead of checking after every movement

a b c d e 
0 1 2 3 4
c d e a b
0 1 2 3 4
a  b  c d e
-3 -3 2 2 2

e a b c d
0 1 2 3 4

a  b  c  d  e
-1 -1 -1 -1 4


'''
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) == 0 and len(goal) == 0:
            return True
        if len(s) != len(goal):
            return False

        firstLetterIndexes = []
        

        for i, char in enumerate(goal):
            if char == s[0]:
                firstLetterIndexes.append(i)
        
        # print('firstLetterIndexes', firstLetterIndexes)
        
        while len(firstLetterIndexes) > 0:
            index = firstLetterIndexes.pop()
            reachedGoal = True
            for i, char in enumerate(s):
                # 0 < 5-1-1
                leftOfIndexAdjusted = index + i # number of left adjustments
                rightOfIndexAdjusted = abs(len(s) - i - index)
                # print('i', i, 's[i]', s[i])
                if i <= len(goal) - index - 1: # of characters adjusted by leftOfIndexAdjusted amount
                    # print('goal[leftOfIndexAdjusted]', goal[leftOfIndexAdjusted],)
                    if s[i] != goal[leftOfIndexAdjusted]:
                        reachedGoal = False
                        break
                else:
                    # print('goal[rightOfIndexAdjusted]', goal[rightOfIndexAdjusted])
                    if s[i] != goal[rightOfIndexAdjusted]:
                        reachedGoal = False
                        break
                # print('\n')
            if reachedGoal:
                return reachedGoal
        return False

'''
time complexity - O(n) since we goal through maximum of 2 times by taking the index difference and comparing it on the second run
space - only firstLetterIndex array so O(k)
'''

sol = Solution()

output = sol.rotateString(s = "abcde", goal = "cdeab")
print(output)

output = sol.rotateString(s = "abcade", goal = "cadeac")
print(output)
