'''
Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.
 

Example 1:


Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [0]
Output: [0]
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
 

Follow up: Can you flatten the tree in-place (with O(1) extra space)?
'''

'''
preorder -> node -> left , then right
change to linked list

if node:
    linkedlist -> node.val
    recursive(left)
    recursive(right)
left pointer always None, right child is the next node in the list
O(1) space

if node:
    left = node.left
    right = node.right
    node.right = left
    node.left = None

O(n) time where n is number of nodes
O(n) space to store right subtree in stack
'''

# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """ 
        # helper will take in the next node and return the stored 
        # right node in a stack
        # O(m) space where m is number of nodes on right side 
        def helper(node: Optional[TreeNode], stack: List[TreeNode]) -> None:
            if node is None:
                return
            left = node.left
            right = node.right
            node.right = left
            node.left = None
            if right:
                stack.append(right)
            helper(node.right, stack)
            if len(stack) > 0:
                node.right = stack.pop()
                helper(node.right, stack)
            
            return
        helper(root, [])
        