"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""

"""
dfs, change and go into left, right, up, down if possible and change original grid data of 1 to 0
increment island by 1
time O(m*n)
space O(1)
remember to only increment island variable outside because we want to change all to 0 in dfs
"""

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        def helper(i: int, j: int) -> None:
            grid[i][j] = '0'

            left, right, up, down = j-1, j+1, i-1, i+1

            if left >= 0 and grid[i][left] == '1':
                helper(i, left)
            if right < cols and grid[i][right] == '1':
                helper(i, right)
            if up >= 0 and grid[up][j] == '1':
                helper(up, j)
            if down < rows and grid[down][j] == '1':
                helper(down, j)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    islands += 1
                    helper(i, j)
        
        return islands

# sol = Solution()
# output = sol.numIslands([
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ])
# print(output)
