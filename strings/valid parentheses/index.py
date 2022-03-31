'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''

'''
dictionary: {
    "}": "{"
}
stack - pop off
if a closing stack doesn't equal opening stack from dictionary return false
return true at the end

O(n) time since we iterating through s
O(1) for space since we know the opening and closing brackets which is only 3 opening/closing. 

What if there's only opening brackets? gotta make a check at the end if len of stack is == 0.
Also what if there's only closing brackets? check if stack is length 0 before popping.
'''
class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            "}": "{",
            "]": "[",
            ")": "("
        }
        stack = []

        for bracket in s:
            if bracket not in brackets: # opening bracket
                stack.append(bracket)
            else: # closing bracket
                if len(stack) == 0:
                    return False
                lastOpeningBracket = stack.pop()
                if brackets[bracket] != lastOpeningBracket:
                    return False
        if len(stack) == 0:
            return True
        return False

sol = Solution()

output = sol.isValid("()")
print(output)

output = sol.isValid("()[]{}")
print(output)

output = sol.isValid("(]")
print(output)
