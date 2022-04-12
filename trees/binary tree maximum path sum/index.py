'''
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

 

Example 1:


Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
Example 2:


Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
 

Constraints:

The number of nodes in the tree is in the range [1, 3 * 104].
-1000 <= Node.val <= 1000
'''

'''
pre-order
L, node, Right
find out if it's better to use L, N, or R or a combination of those
by seeing if values of each greater than 0

gotta make another function and a maxSum variable in init because
if we return max of every position up, say if it's only right that's biggest,
we can't have it add that with the parent's node, skipping the node.
O(n) time complexity
O(1) space
'''

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.maxSum = float('-inf')
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def helper(root: Optional[TreeNode]) -> int:
            left, node, right = float('-inf'), root.val, float('-inf')
            if root.left:
                left = helper(root.left)
            if root.right:
                right = helper(root.right)
            print('node', node)
            print(left, right)
            self.maxSum = max(self.maxSum, left, left+node, left+node+right, node, node+right, right)
            return max(left + node, node, node + right)
        helper(root)
        return self.maxSum