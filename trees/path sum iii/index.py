'''
Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

 

Example 1:


Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.
Example 2:

Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3
 

Constraints:

The number of nodes in the tree is in the range [0, 1000].
-109 <= Node.val <= 109
-1000 <= targetSum <= 1000
'''

'''
we are going all the way to the bottom
we are going to return left value, node val, and right val
add the current node val to all 3 then return it to it's parents

time - O(n)
space - O(3n)?
what ;if we get a 0 answer? 1 -> -1 -> 8 if target is 8?

'''

# Definition for a binary tree node.
from typing import List, Optional, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        output = 0

        if root is None:
            return output
        
        def helper(node: Optional[TreeNode]) -> List[int]:
            if node is None:
                return []
            left = helper(node.left) # [3]
            right = helper(node.right) # [-2]
            
            for num in left:


            # we are not at a leaf node
            if len(left) > 0:
                leftValue = left.val + node.val
            # we are not at a leaf node
            if len(right) > 0:
                rightValue = right.val + node.val
            return (leftValue, node.val, rightValue)
            
        
        helper(root)
        return output
