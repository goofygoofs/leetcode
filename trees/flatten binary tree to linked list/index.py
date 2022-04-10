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

'''
when they say they want it to be flatten to pre-order traversal, that means the
root node goes first, then next is process the left subtree, then the right subtree
once we have flattened the entire left subtree, we have to return a pointer to the last node
or rather the tail of the linked list. if we have the tail of the linked list, then we can
connect that pointer over to the right child of the root node. so we have to return the tail of
the linked list
since we are traversing the tree the space will be O(h) height of tree
to get the last pointer, return rightTail or leftTail or node
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
        # flatten the root tree and return the list tail
        def helper(node: Optional[TreeNode]) -> Optional[TreeNode]:
            if node is None:
                return None
            leftTail = helper(node.left)
            rightTail = helper(node.right)

            # only do insert operation if leftTail has a node
            if leftTail:
                leftTail.right = node.right
                node.right = node.left
                node.left = None
            last = rightTail or leftTail or node
            return last

        helper(root)
        