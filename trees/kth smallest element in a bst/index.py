'''
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

 

Example 1:


Input: root = [3,1,4,null,2], k = 1
Output: 1
Example 2:


Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
 

Constraints:

The number of nodes in the tree is n.
1 <= k <= n <= 104
0 <= Node.val <= 104
 

Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?

'''

'''
go to smallest one => keep going left
then go pre-order
left, node, right
go up until it's k smallest
since we know order because it's binary tree
O(k + lgn) time
O(lgn) space for stack 
'''

'''
binary search tree means everything in left subtree is less < node.val < right.val
any way we can put it in a sorted array?

'''

# Definition for a binary tree node.
from typing import Optional, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # use array to modify by reference
        output = [k, 0]
        def helper(node: Optional[TreeNode]) -> None:
            # return early if 0
            if output[0] == 0:
                return
            if node.left:
                helper(node.left)
            output[0] -= 1
            if output[0] == 0:
                output[1] = node.val
            if node.right:
                helper(node.right)

        helper(root)
        return output[1]
