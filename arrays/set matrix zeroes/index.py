'''
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

 

Example 1:


Input: matrix = 
[[1,1,1],
 [1,0,1],
 [1,1,1]]
Output: 
[[1,0,1],
 [0,0,0],
 [1,0,1]]
Example 2:


Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 

Constraints:

m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1
 

Follow up:

A straightforward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
'''

'''
loop through once, find out all indicies of 0 (x,y) position
then loop again, any x position turn into 0, any y position turnt 0

create x set and y set
O(m*n) time complexity
this is O(m + n space)

can i do it in O(1) space?
'''

'''
there's a bunch of ways to solve this problem. first show bad solution then the constant space solution
straight way is create a copy O(m*n) space. when we make change we will make changes on our copy and when we read values
we will read from our input. having a copy is probably not best solution best we are doing repeated work as we read from input 
and several values get re-set to 0.

we have a certain set of rows, and certain set of columns. so we just have to iterate through every row and column
which is O(m + n). we can have 1 array for number of columns and one arrayt
for number of rows. and we can mark these with True or false, whether we want to fill these with 0 or not.
initialize the row and column arrays with False. if we find a zero, both arrays get marked True
the advantage of this is we only need to create 2 arrays of m and n size

can we get a O(1) memory solution?
best time complexity is O(m*n) time complexity because we have to go through every position in the matrix
is it possible to take this array and put it into our matrix?
we can take this array we have an put it into our matrix
notice how the 2 arrays are overlapping
we just need 1 more variable for the overlapping cell from the row and column arrays
we dont need extra memory from input array but we do need 1 extra cell
 
when we iterate through, the 0 in the position is going to tell us this column needs to be 0 out
and the extra cell we will mark 0 to tell us that this row needs to be 0 out

as we iterate through the 2nd row, if we set the first row's col's cell to 0, indicating that the column needs to be zeroed out
to set the 2nd row to 0, we can go back and set it because we work out way from left to right

so the top left extra cell indicates if the first row needs to be zeroed out since it overlaps. but for all other rows if a 0 is in the first index,
then that row needs to be zeroed out.
'''
from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # O(1) space
        rows, cols = len(matrix), len(matrix[0])

        # for overlapping cell, to calculate if first row needs to be zerod
        rowZero = False

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0 # if we find a zero, set the first row for that column equal to zero

                    if r > 0:
                        matrix[r][0] = 0 # only if row > 0
                    else: # for only first row, if zero, we set our extra cell to 0 so we can zero out the column later
                        rowZero = True
        
        # go over again and zero out
        # have to skip out the first row and first column
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        
        # if it's already zero for 1st row 1st col
        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0
        
        # if our overlap is true, then zero our first column
        if rowZero:
            for c in range(cols):
                matrix[0][c] = 0


        
        return matrix

# sol = Solution()

# output = sol.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]])
# print(output)