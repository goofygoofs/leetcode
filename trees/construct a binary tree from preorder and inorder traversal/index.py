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

'''
given 2 integer arrays representing preorder and inorder traversals of a binary tree. it has all
the info we need. we just need to take info and deconstruct it and construct the original binary tree
preorder - process at root (node) and then left subtree. then right subtree
    first value always the root(node)
inorder - starts at the leftmost subtree processing left first, then process node, then right subtree
    first value always the left node
every value in the traversal is unique because it is binary tree
every value to the left of the first value of pre-order in inorder is going in the left subtree of the root
and every value to the right of the first value of pre-order in inorder is going in the right subtree
what we can do is take the remainder of what's in the pre-order array and partition it
we know 1 value is going in the left subtree and 3 values are going in the right subtree
we're going to do this recursively
the first value to the right of the root is the node in preorder
find 20 (mid) we don't need 20 anymore. there's 1 value on the left of 20 and 1 value on the right of 20
contstruct that left subtree with the 1 value and the right subtree with the 1 value
once we find mid (which is first value in pre-order) we can find the lenght of the left subtree (left subarray) and right subtree(right subarray)
these counts tell us how to partition the pre-order traversel
from that partition it tells us how many nodes go in the left subtree (run recursively), and for right subtree (run recursively)
always start with base case. no nodes

time - O(n + 1/2n?)
space - O(n) for splicing + O(h) for stack
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
        if not preorder or not inorder:
            # don't need to create a tree
            return None
        
        # root always going to be the first value
        root = TreeNode(preorder[0])
        # tells us the length of how many nodes in the left subtree
        mid = inorder.index(preorder[0])
        # left subtree will be built with up to the mid length
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root