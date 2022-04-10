'''
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [1,2], p = 1, q = 2
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the tree.
'''

'''
recursion
we need to somehow pass level, lowest level and the node
return the lowest node on the lowest level that contains both p and q
LCA is determined by check if p and q exist in => left subtree, node, and right subtree.
only 1 each
all unique values

O(n) time
O(h) space
'''
# Definition for a binary tree node.
from typing import Optional, Tuple


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: Optional[TreeNode], p: Optional[TreeNode], q: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def helper(node: Optional[TreeNode], p: int, q: int) -> Tuple[bool, TreeNode]:
            if not node:
                return (False, None)
            containLeft = helper(node.left, p, q)
            containNode = node.val == p or node.val == q
            containRight = helper(node.right, p, q)

            isLCA = 0 
            if containLeft and containLeft[0]:
                if containLeft[1]:
                    return containLeft
                isLCA += 1
            if containNode:
                isLCA += 1
            if containRight and containRight[0]:
                if containRight[1]:
                    return containRight
                isLCA += 1

            if isLCA == 2:
                return (True, node)
            if isLCA == 1:
                return (True, None)

            return (False, None)

        return helper(root, p.val, q.val)[1]
