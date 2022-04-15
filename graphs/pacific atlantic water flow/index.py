'''
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

 

Example 1:


Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Example 2:

Input: heights = [[2,1],[1,2]]
Output: [[0,0],[0,1],[1,0],[1,1]]
 

Constraints:

m == heights.length
n == heights[r].length
1 <= m, n <= 200
0 <= heights[r][c] <= 105
'''

'''
return list of cordinartes [[1,2],[2,3]]..,etc where that coordinate can flow to 
both pacific and atlantic. 
pacific is top and left
atlantic is bottom and right
we can start from the edge and dfs/bfs to areas greater than or equal to those coordinates at the edges
then do that for both oceans and compare the matching coordinates (we can compare via a set)
then for the matching, we add it to the output

get all coordinates for pacific and atlantic

time is O(n) where n is number of coordinates or nodes in the graph
space is O(n) to create sets
'''

from typing import List, Set, Tuple


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.row = len(heights)
        if self.row == 0:
            return []
        self.col = len(heights[0])
        if self.col == 0:
            return []

        pacific = []
        atlantic = []
        pacificReach = set() # Set of Tuple because list is unhashable
        atlanticReach = set()
        bothReached = []

        for i in range(self.row):
            pacific.append((i, 0))
            pacificReach.add((i, 0))
            atlantic.append((i, self.col-1))
            atlanticReach.add((i, self.col-1))
        
        for i in range(self.col):
            pacific.append([0, i])
            pacificReach.add((0, i))
            atlantic.append((self.row-1, i))
            atlanticReach.add((self.row-1, i))

        def helper(coordinate: Tuple[int], visited: Set[Tuple[int]]) -> None:
            i, j = coordinate[0], coordinate[1]
            left, right, up, down = j-1, j+1, i-1, i+1
            if left >= 0 and (i, left) not in visited and heights[i][left] >= heights[i][j]:
                visited.add((i, left))
                helper((i, left), visited)
            if right < self.col and (i, right) not in visited and heights[i][right] >= heights[i][j]:
                visited.add((i, right))
                helper((i, right), visited)
            if up >= 0 and (up, j) not in visited and heights[up][j] >= heights[i][j]:
                visited.add((up, j))
                helper((up, j), visited)
            if down < self.row and (down, j) not in visited and heights[down][j] >= heights[i][j]:
                visited.add((down, j))
                helper((down, j), visited)

        for coordinate in pacific:
            helper(coordinate, pacificReach)
        
        for coordinate in atlantic:
            helper(coordinate, atlanticReach)
        
        for reached in pacificReach:
            if reached in atlanticReach:
                bothReached.append([reached[0], reached[1]])
        
        return bothReached

sol = Solution()
output = sol.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]])
print(output)