"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
Example 2:


Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
 

Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000
"""

"""
[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

[
    [7,4,1],
    [8,5,2],
    [9,6,3]
]

create a dictionary where once we visit a position, we will update it with the translated position. take the original value,
store it in a dictionary with the row, col as a key. we check the row,col key before making any updates, and remove it once updated. if there's no 
row value key in dict, that is the original number

time complexity - O(n * m) traverse all rows and cols
space - O(max(m,n)) since at max we storing 1 row or col at a time before it gets deleted by going into the next one
"""
from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        seen = {}

        rows, cols = len(matrix), len(matrix[0])

        for r in range(rows):
            for c in range(cols):
                # original number
                # if (r, c) not in seen:
                # store original number
                seen[(r,c)] = matrix[r][c]
                # check for original number for replacing
                inverse = (c, rows - r - 1) # 0, 2-2
                # original number here
                original = (cols - inverse[0] - 1, r)
                if original not in seen:
                    matrix[r][c] = matrix[original[0]][original[1]]
                    # print('matrix', matrix)
                else: # replace with original from seen
                    # print('here')
                    matrix[r][c] = seen[original]
                # not original number. (r, c) in seen which is the original number 
                # else: 
        return matrix
sol = Solution()

output = sol.rotate([[1,2,3],[4,5,6],[7,8,9]])
print(output)
        
