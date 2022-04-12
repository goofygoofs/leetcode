'''
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

 

Example 1:


Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]
Example 2:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-1000 <= Node.val <= 1000
'''

'''
we are given 2 binary trees and we want to write 2 functinos for it
serialize aand deserialize
serialize we're taking an object in memory can be anything this node can be anywhere there's links connecting them anywhere
put it in an easy to read string
convert this entire tree into a string
and we want to take a string like this and turn it into a tree
can use BFS taking it level by level serializing the tree
check for 'None' string in deserializing
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        queue = deque([root])
        output = ""

        while len(queue) > 0:
            nextLevel = deque()
            while len(queue) > 0:
                node = queue.popleft()
                if not node:
                    output += "None,"
                else:
                    output += str(node.val) + ","
                    if node.left:
                        nextLevel.append(node.left)
                    else:
                        nextLevel.append(None)
                    if node.right:
                        nextLevel.append(node.right)
                    else:
                        nextLevel.append(None)
            if len(nextLevel) > 0:
                queue = nextLevel
        return output[:-1]

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        # [1,2,3,null,null,4,5]
        # [2,3,null,null,4,5]
        # [null,null,4,5]
        queue = deque(data.split(','))
        root = TreeNode(queue.popleft())
        # []
        treeQueue = deque([root])
        
        # left 2
        # right 3

        while len(queue) > 0:
            nextLevel = deque()
            while len(treeQueue) > 0:
                node = treeQueue.popleft()
                left, right = queue.popleft(), queue.popleft()
                if left != 'None':
                    left = TreeNode(left)
                else:
                    left = None
                node.left = left
                if right != 'None':
                    right = TreeNode(right)
                else:
                    right = None
                node.right = right
                # check if add to next level
                if left != None:
                    nextLevel.append(left)
                if right != None:
                    nextLevel.append(right)
            if len(nextLevel) > 0:
                treeQueue = nextLevel
        return root
            


        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))