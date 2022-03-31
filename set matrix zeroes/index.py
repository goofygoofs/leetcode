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
this is O(m + n space)
'''
from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        xSet = set()
        ySet = set()

        for i in range(len(matrix)):
            row = matrix[i] # [1, 1, 1]
            for j in range(len(row)):
                value = row[j] # 1
                if matrix[i][j] == 0:
                    xSet.add(i)
                    ySet.add(j)

        for i in range(len(matrix)):
            row = matrix[i] # [1, 1, 1]
            for j in range(len(row)):
                if i in xSet or j in ySet:
                    matrix[i][j] = 0
        
        return matrix

# sol = Solution()

# output = sol.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]])
# print(output)