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

from typing import List, Tuple


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row = len(matrix)
        col = len(matrix[0])
        order = [(0, 1), (1, 0), (-1, 0), (0, -1)] # right, down, up, left
        self.timesNotRotated = 0 # keep track of how many times we did not rotate, if 4, we are done
        self.index = 0 # keeps self.index for order
        self.coordinate = (0, 0)
        visited = set()
        visited.add(self.coordinate)
        output = [matrix[0][0]]

        def helper() -> None:
            while (self.coordinate[0] + order[self.index][0], self.coordinate[1] + order[self.index][1]) not in visited \
                and ((self.index in (0,3) and self.coordinate[1] + order[self.index][1] >= 0 and self.coordinate[1] + order[self.index][1] < col) \
                or (self.index in (1,2) and self.coordinate[0] + order[self.index][0] >= 0 and self.coordinate[0] + order[self.index][0] < row)):
                
                self.coordinate = (self.coordinate[0] + order[self.index][0], self.coordinate[1] + order[self.index][1])
                visited.add(self.coordinate)
                output.append(matrix[self.coordinate[0]][self.coordinate[1]])
                self.timesNotRotated = 0
        while self.timesNotRotated != 4:
            helper()
            self.index += 1
            if self.index > 3:
                self.index = 0
            self.timesNotRotated += 1
        return output

sol = Solution()
output = sol.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(output)



