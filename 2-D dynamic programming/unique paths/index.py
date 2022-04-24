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

'''
how many unique path to get to itself (at the bottom right) = 1
all values out of bounds are 0
value of all bottom row is 1
amount of unique paths res at any space is equal to D + R (because if we store it in cache we dont have to run again because we know
the amount of unique paths there  )
28  21  15  10  6   3   1 0                       
7   6   5   4   3   2   1 0
1   1   1   1   1   1   1 0
0   0   0   0   0   0   

create dp row and calculate for node is right + down
for i
    create new row
    for j 
        update node value
    update row = new row
time - O(m*n)
space - O(n) for row array
'''

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n # since we know bottom row is all 1's
        for i in range(m - 1): # skip last row since we know it's all 0's
            newRow = [1] * n
            for j in range(n-2, -1, -1): # we know entire last col is 1, so we skip it
                newRow[j] = newRow[j + 1] + row[j] # newRow(curr row) on it's right side and the space directly down
            print(newRow)
            row = newRow
        return row[0]

sol = Solution()
output = sol.uniquePaths(3, 7)
print(output)