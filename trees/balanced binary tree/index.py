'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:


Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true
 

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104
'''

'''
recursive return left == right
each time go down left and rigth, add 1 for each layer
can't be more difference by 1
'''

'''
what is defined as height balanced?
height of left subtree is 1
height of right subtree is 2
difference is 1
that also means each left and right subtree has to be balanced too so one that goes down just left.left.left with no rights is not balanced
if we go through each node, we have to do an O(n) operation where n is number of nodes
and we do this operation n times, we're going to get a time complexity of O(N^2)
can we do better than that, is there any repeated work?
yes there is repeated work and it can be eliminated by 
asking the question in a different order. instead of first asking if the entire tree is balanced 
from the root node, we ask is it balanced starting from here instead of asking that we do this bottom up
we ask is this entire subtree balanced, until we keep going lower and lower until
we get to the base case once we get to the base case
we going to go back up and show how that's actually going to eliminate the repeated work
if we do it in this order. we'll only have to visit each node at most one time to ensure
overall time complexity is O(n) instead of n^2
we return the height of each subtree on the left and right
and take the difference between those
going to return a boolean as the first value and the height as the 2nd value
if we ever find False, we gotta return False at the root
'''

# Definition for a binary tree node.
from typing import Optional, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        

        def helper(root: Optional[TreeNode]) -> Tuple[bool, int]:
            if root is None:
                return (True, 0)
            left, right = helper(root.left), helper(root.right)
            leftBalanced, rightBalanced = left[0], right[0]
            difference = abs(left[1] - right[1])
            balanced = (leftBalanced and rightBalanced and difference <= 1)
            return (balanced, 1 + max(left[1], right[1]))

        return helper(root)[0]


tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(2)
left = tree.left
left.left = TreeNode(3)
left = tree.left
left.left = TreeNode(4)

sol = Solution()
output = sol.isBalanced(tree)
print(output)