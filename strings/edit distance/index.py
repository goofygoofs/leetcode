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

'''
DYNAMIC PROGRAMMING
this is a problem very similar to longest common subsequence basically an extension
we are given 2 words are given the requirement of returning the minimum number of operations required
to convert word 1 to word 2
only have 3 operations available. we can't change word 2. we can only change word 1
like analyze a few cases
both word 1 and word 2 are empty strings or both "abc" then 0 operations

what if word1 was abc and word2 is empty. it's possible, we can remove characters.
it's always going to take the length of word1 if word 2 is empty.
what if word2 is abc and word 1 is empty? we can insert characters and insert
so the operations is going to be length of word2.
if one of them is empty, we are going to return the length of the non-empty string

brute force?
one pointer pointer at word1 and one pointer at word 2.
what if they are exactly equal? what is the sub-problem then right? because we don't have to consider 
these characters anymore. now we're dealing with the sub problem of the remainder of those strings 
so basically if im calling pointer in word one i and calling the pointer in word 2 j. if both of these are equal, we can basically say
the new problem is everything after, i+1 and j+1 are new subproblems.

if these 2 characters are equal at the i and j pointers
word1 = abd
word2 = acd
i[0] == j[0]
if equal, then increment i by 1 and increment j by 1
if w1[i] == w2[j]:
    i += 1
    j += 1
else: # if they don't equal we can either insert, delete or replace

equal (i + 1, j + 1)
num of operation is 0

insert (i, j+1)
but which one do we do, don't know so we do all 3 (insert, delete, and replace)
if we insert, i pointer stays the same but j increments by one. because the new character gets inserted before the index

delete (i + 1, j)
take i pointer and shift it to the next position. we leave the j pointer there.

edit (i + 1, j + 1)
if we edit a character we want the character that is matching. if we did that the 2 characters will match
edit does exact same thing as if they were equal. takes 1 operation

notice now when we have 2 empty strings once we are at the end. empty string is 0 operations and that 
is what happens when we reach the end.

the subproblems are good to solve before solving the problem of comparing the entire list
this is going to be a 2-dimensional dynamic programming problem. it's good to visualize it kind of liek this
  a c d      w2(j axis)
a 0 1 1 3    
b 1 1 1 2    
d 1 1 0 1    
  3 2 1 0
w1(i axis)
so what we are doing here we want to calculate. in this position we're
going to want to store the minimum number of operations for these 2 strings starting at this character for word 2 and these for word1 so basically
the entire strings is going to be stored here. what would be stored in this position
at the intersection of b and c is the minimum operations it would take to make this subproblem which are these two sub strings
how many minimum operations it would take to make them equal
why do i have this extra row and column over here (1 extra row and column after the d and d for word 1 and word 2)
this portion is for our base case
at the intersection of empty row and column it would be 0
at the begining of the empty column how long would it be, remember we did before
if empty string, it will be length of the rest of the string
so at 2nd empty, it would be "a" and "acd" so it takes 2

so in what order are we going to solve thnis? if we start at the beginning, we are going to notice something
notice we are comparing these 2 characters at this position. they both are equal right so we're going to
then we are going to take the result of that which is (i+1, j+1)
what does that give us? it will depend on the value c == b? if they are not equal, we have to brute force all three methods
what we are going to do is insert with give us (i, j+1) so starting at (1,1) we will get (1, 2)
and delete will give us (i+1, j) which is (2,1). for replace we are going diagonal to (2,2)
which one of 3 leads us to the minimum operation?
let's do this bottom up, aka bottom up dynamic programming
if we do start in bottom right so bottom right empty 0 -> 0 (d,d), b,c(1,1) and a,a(0)

this is exactly what we're doing in the code. going to have a 2d array and execute these 3 statements 
'''
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # we do need to make our 2d array 1 bigger for base cases
        # cahce is our 2d array
        '''
        [
            ["inf","inf","inf",5],
            ["inf","inf","inf",4],
            ["inf","inf","inf",3],
            ["inf","inf","inf",2],
            ["inf","inf","inf",1],
            [ 3,    2,    1,   0]
        ]
        '''
        cache = [[float("inf")] * (len(word2) + 1) for i in range(len(word1) + 1)] 

        # now for our cache we want to go to the bottom row and it's going to be the length of word1
        # go through every value (j) of it
        # basically initializing base case of our 2d array
        for j in range(len(word2) + 1):
            cache[len(word1)][j] = len(word2) - j
        for i in range(len(word1) + 1):
            cache[i][len(word2)] = len(word1) - i
        # print(cache)
        # now lets get into dynamic programming. remember bottom up so we work our way backwards
        # reason we start at len(word1) -1 because we already filled base case
        # for i in range(len(word1) - 1): we are going to do this in decrementing order until we get to 0 index
        # remember we are starting on the bottom row in the last column (not the extra cell base case one) and working our way to the top
        for i in range(len(word1) -1, -1, -1):
            for j in range(len(word2) -1, -1, -1):
                if word1[i] == word2[j]: # remember when they are equal it is easy. it does not take an operation and we just shift (i+1, j+1)
                    cache[i][j] = cache[i+1][j+1]
                else: # if it's anything else it will be 1 + min of those 3 direction
                    # taking care of insert, delete, and edit and minimum of what those were
                    # and adding 1 operation whatever it was to it
                    cache[i][j] = 1 + min(cache[i+1][j], cache[i][j+1], cache[i+1][j+1])

        # once we fill up entire 2d array, we want to return the value at index 0,0 of our cache because that 
        # tells us the minimum number of operations of both strings so basically the entirety of both strings 
        return cache[0][0]

'''
time is O(n*m) to go through each position in the 2d array
space is also O(n*m)
'''

sol = Solution()

output = sol.minDistance(word1 = "horse", word2 = "ros")
print(output)

output = sol.minDistance(word1 = "intention", word2 = "execution")
print(output)
