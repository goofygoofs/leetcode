'''
Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
'''

'''
clockwise order
mxn matrix => array
starts off at the top left, goes clockwise, inwards

m, n are within base case boundaries

(right, down, left, up, right...)
function that will keep iterating until it reaches a wall,
visited (x, y)
once we've reached where we cannot move anymore, we are done

O(mxn) time m col, n rows
O(n) mxn for the output array

create a set first then add tuple to set.
tuples are immutable
lists are mutable
only immutable are allowed to be added to set
if you initialize set with tuple in it, it will be different, always add to set afterwards

'''

'''
can do with O(1) space using left and right boundaries instead of a set
update boundaries whenever we complete an entire row or column. the matrix gets smaller
when reverse, sure you take the reverse -1 and the ending -1 to include the initial number

'''

from typing import List, Tuple


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left, right = 0, len(matrix[0]) # column boundaries
        top, bottom = 0, len(matrix) # row boundaries

        while left < right and top < bottom:
            # get every i in the top row
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1

            # get every i in the right col
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1

            # catches cases if single row or single col
            if not (left < right and top < bottom):
                break
            
            # get every i in the bottom row
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1

            # get every i in the left row
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
        return res


sol = Solution()
output = sol.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(output)



