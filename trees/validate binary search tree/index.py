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

'''
valid BST 
every node in left subtree is less than node.val
every node in right subtree is greater than node.val
left boundary (-inf < 3 < 5)
right boudnary (5 < 7 < inf)
right boundary (7 < 8 < inf)
left boundary (5 < 4 < 7) No, this breaks our boundary

gotta use OR instead of left <= node.val <= right
so it will be
left<= node.val or node.val <= right

time - O(n)
space - O(h) height of tree because of recursion
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

        def helper(node: Optional[TreeNode], left: int, right: int) -> bool:
            if not node:
                return True

            if left >= node.val or node.val >= right:
                return False
            
            return helper(node.left, left, node.val) and helper(node.right, node.val, right)

        return helper(root, float("-inf"), float("inf"))

