'''
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
'''

'''
while loop if queue is not length 0,
actually have to add an array that appends into the loop
we loop through that and get all it's non -none left and rights, add to array, 
go from left to right so we need to use queue

O(n) for time 
O(level) for space
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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # queue is a list of TreeNodes
        if root is None:
            return []
        queue = deque([root])
        output = []
        while len(queue) > 0:
            values = []
            treeNodes = []
            while len(queue) > 0:
                node = queue.popleft()
                values.append(node.val)
                if node.left:
                    treeNodes.append(node.left)
                if node.right:
                    treeNodes.append(node.right)
            output.append(values)
            if len(treeNodes) > 0:
                queue = deque(treeNodes)
        return output
