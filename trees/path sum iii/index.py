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

'''
get current sum as going down, not from bottom up
if current sum (node.val + whatever preivous from parent) - targetSum = 0 (we have a match)
then subtract the target from the currSum to see if any previous nodes adds up to the targetNum
we use a dict that increments currSum and adds if that currSum - targetSum becuase there can be targetSum on both sides
so it will go up by a certain amount if another target num comes in on the other side
we then remove mapping[currSum] -= 1 as we backtrack
'''
# Definition for a binary tree node.
from typing import List, Optional, Tuple
from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # arrays works better with python's namespace and updating the first value
        # using a variable will have scope issues in this way
        output = [0]
        def helper(node: Optional[TreeNode], currSum: int) -> None:
            if not node:
                return
            currSum += node.val
            if currSum - targetSum in mapping:
                output[0] += mapping[currSum - targetSum]
            mapping[currSum] += 1
            # print('node.val', node.val)
            # print('mapping', mapping)
            # print('output', output)
            helper(node.left, currSum)
            helper(node.right, currSum)
            mapping[currSum] -= 1
        mapping = defaultdict(int)
        mapping[0] = 1
        helper(root, 0)
        return output[0]

tree = TreeNode(5)
left = TreeNode(3)
tree.left = left
left = tree.left
left.left = TreeNode(-1)
left = left.left
left.left = TreeNode(1)
left = left.left
left.left = TreeNode(8)

sol = Solution()

output = sol.pathSum(tree, 8)
print(output)