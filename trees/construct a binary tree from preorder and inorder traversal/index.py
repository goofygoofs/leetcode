'''
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

 

Example 1:


Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]
 

Constraints:

1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder and inorder consist of unique values.
Each value of inorder also appears in preorder.
preorder is guaranteed to be the preorder traversal of the tree.
inorder is guaranteed to be the inorder traversal of the tree.
'''

'''
pre-order - will keep going left, (node unless already visited), then right
in-order will start at the left most, the local node, the right, go up to the next node, then right
get the root from the pre-order first
keep going in pre-order until it hits first of in order (left most root)
then get the right from in-order
use queue on both
'''

# Definition for a binary tree node.
from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorder = deque(preorder)
        inorder = deque(inorder)
        root = TreeNode(preorder.popleft())
        curr = root

        # remove first inorder if equal to preorder root
        if root.val == inorder[0]:
            inorder.popleft()
        
        def helper(node: Optional[TreeNode]) -> None:
            if len(preorder) > 0 and len(inorder) > 0:
                left = TreeNode(preorder.popleft())
                node.left = left
                # can still keep going left until leftmost leaf
                if left.val != inorder[0]:
                    helper(node.left)
                else:
                    while inorder[0] != node.val:
                        inorder.popleft()
                    inorder.popleft()
                    preorder.popleft()
                right = TreeNode(inorder.popleft())
                node.right = right

        if len(preorder) > 0:
            helper(curr)
        return root