'''
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:


Input: root = [2,1,3]
Output: true
Example 2:


Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
'''

'''
recursive, and return a Tuple (bool, val)
if bool if any False, return False. check value if checks out. if False, return false
use AND to compare
'''

# Definition for a binary tree node.
from typing import Optional, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # returns (bool, TreeNode, min: int, max: int)
        def helper(node: Optional[TreeNode]) -> Tuple[bool, TreeNode, int, int]:
            if node is None:
                return (True, None, float('inf'), float('-inf'))
            left = helper(node.left)
            right = helper(node.right)
            # stop early if any False
            if left[0] is False or right[0] is False:
                return (False, None, float('inf'), float('-inf'))

            # check min and max of entire tree
            # also check left vs right subtree min and maxes
            if left[2] >= node.val >= right[2] or left[3] >= node.val >= right[3] \
                or left[2] >= right[2] or left[3] >= right[3]:
                return (False, None, float('inf'), float('-inf'))
            # check local validity
            if left[1] and right[1]:
                if left[1].val >= node.val >= right[1].val:
                    return (False, None, float('inf'), float('-inf'))
            if left[1]:
                if left[1].val >= node.val:
                    return (False, None, float('inf'), float('-inf'))
            if right[1]:
                if node.val >= right[1].val:
                    return (False, None, float('inf'), float('-inf'))
            return (left[0] and right[0], node, min(node.val, left[2], right[2]), max(node.val, left[3], right[3]))

        return helper(root)[0]
