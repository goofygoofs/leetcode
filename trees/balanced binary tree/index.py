'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:


Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true
 

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104
'''

'''
recursive return left == right
each time go down left and rigth, add 1 for each layer
can't be more difference by 1
'''

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        

        def helper(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0
            left = helper(root.left)
            right = helper(root.right)
            return max(1 + left, 1 + right)
        
        left = helper(root.left)
        right = helper(root.right)

        return left == right or left + 1 == right or left == right + 1


tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(2)
left = tree.left
left.left = TreeNode(3)
right = tree.right
right.right = TreeNode(3)
left = tree.left
left.left = TreeNode(4)
right = tree.right
right.right = TreeNode(4)

sol = Solution()
output = sol.isBalanced(tree)
print(output)