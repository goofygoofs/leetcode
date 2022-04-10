'''
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

 

Example 1:


Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
Example 2:


Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
 

Constraints:

The number of nodes in the root tree is in the range [1, 2000].
The number of nodes in the subRoot tree is in the range [1, 1000].
-104 <= root.val <= 104
-104 <= subRoot.val <= 104
'''

'''
subtree does not return true if you compare, gotta compare the values
if we see a matching value, we recursion through all the nodes to compare. anything that doesn't match
break out

time - O(n * m) have to go through subroot (m) if intially value is same
space - O(m) space for stack
'''

# Definition for a binary tree node.
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def helper(node: Optional[TreeNode], subNode: Optional[TreeNode]) -> bool:
            if node is None and subNode is None:
                return True
            if node is None:
                return False
            if subNode is None:
                return False
            if node.val != subNode.val:
                return False
            return helper(node.left, subNode.left) and helper(node.right, subNode.right)

        queue = deque([root])
        while len(queue) > 0:
            node = queue.popleft()
            left, right = node.left, node.right
            if node.val == subRoot.val:
                if helper(left, subRoot.left) and helper(right, subRoot.right):
                    return True
            if left:
                queue.append(left)
            if right:
                queue.append(right)
 
        return False


