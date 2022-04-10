'''
Given the root of a binary tree, invert the tree, and return its root.

 

Example 1:


Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
Example 2:


Input: root = [2,1,3]
Output: [2,3,1]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
'''

'''
what is invert?,
swap the left with the right subtree
case where there is a left node but no right?
set root.left = right
vice versa
time: O(n) where n is # of nodes
space: O(n) for number for stacks for recursion 
'''

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        def helper(root: Optional[TreeNode]) -> Optional[TreeNode]:
            if root is None:
                return None
            left = root.left
            right = root.right
            root.left = helper(right)
            root.right = helper(left)
            return root
        return helper(root)