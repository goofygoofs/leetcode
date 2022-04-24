'''
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

 

Example 1:


Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
 

Constraints:

1 <= m, n <= 100
'''

'''
dfs, set (don't think we need)
2 choices, down or right
O(2^(m*n)) time
until we reach 0,0
'''

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        self.count = 0
        self.row = m
        self.col = n
        def helper(m: int, n: int) -> None:
            # go down and right
            if m + 1 in range(0, self.row):
                helper(m+1, n)
            if n + 1 in range(0, self.col):
                helper(m, n+1)
            if m == self.row - 1 and n == self.col - 1:
                self.count += 1

        helper(0, 0)
        return self.count    