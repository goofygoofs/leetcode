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

'''
time complexity O(n^2) because nxn matrix
space is O(1) because we are doing this in place 

set some boundaries, left boundary and right boundary because we are going to rotate the outermost layer first
then we will move inwards
top boundary and bottom boundary
    left       right
top  5   1  9  11
     2   4  8  10
     12  3  6  7
     15  14 12 16
bottom

general rotation is clockwise 
we are going to do that for every element in the top row.
for the 1, it is offset by 1, and will be offset by one for the 2nd position
for the last 4 elements, it will be a square rotation. we actually are doing only 3 rotations
since the 1st element is at the top right
so even though outer layer is n*n, we actually did n-1 rotations
n*n => (n-1) rotations  => 3 rotations

then we have an inner matrix we need to do.
it can be treated as a subproblem. we know it's a square matrix. we just shift our boundaries by 1
so we shift our left, right, top, bottom boundaries, then we shift.
we shift one last time but that gives us R<L and we know L should not cross R side

we need a temporary variable before shifting
we know 5 will be rotated, let's do rotation in reverse order. let's take the 15 and put over there. move 5 to temporary variable
don't move 5 now, let's take 16 and move to bottom left. then move 11 to bottom right. 
then original 5 move over to top right
we did exact same rotation but counter clockwise and the helpful thing is we only need 1 temporary variable for the 5
'''
from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # first set left and right boundaries
        # number of columns = number of rows since it is n*n, or a square
        l, r = 0, len(matrix[0]) - 1

        # run our rotation
        while l < r:
            # go from the entire row except the last element
            for i in range(r - l): # 0, 3 => 3 iteration even though we have 4 values in the row
                top, bottom = l, r # top and bottom the same since we have a square

                # save the topLeft
                topLeft = matrix[top][l + i]

                # move bottom left into top left
                matrix[top][l + i] = matrix[bottom - i][l]

                # move bottom right into bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # move top right into bottom right
                matrix[bottom][r - i] = matrix[top + i][r]

                # move top left into top right. but remember we overrode top left position but stored it in temp variable
                matrix[top + i][r] = topLeft
            
            # update our pointers
            r -= 1
            l += 1
        


sol = Solution()

output = sol.rotate([[1,2,3],[4,5,6],[7,8,9]])
print(output)
        
