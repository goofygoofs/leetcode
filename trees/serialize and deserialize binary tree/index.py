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

can do it by DFS using pre-order traversal - this uses less code
root node is 1., then do left subtree. then right subtree. use comma as a delimiter
"1,2,N,N,3,4,N,N,5,5,N,N"
is this string ambiguous? do we know which goes to left or right subtree?
we are going to have a string and split it to an array
how do we know when the left subtree stops and when the right subtree starts?
if it's a Null we can't continue anymore
we reach our base case if both children is Null
next value (3) is the right child of 1. for 4, both children is Null so the right of 3 is 5
then both children of 5 is Null
for every single leaf node we specific all the Nulls
that's why it's not ambigious
O(n) for serializing and deserializing
O(n) for the string and array
for serializing, use an array, then join by "," at the end to avoid extra commas
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
        output = []

        def helper(node):
            if not node:
                output.append("N")
                return
            output.append(str(node.val))
            helper(node.left)
            helper(node.right)
        helper(root)
        return ",".join(output)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(",")
        # because we want it to be global pointer
        self.i = 0

        def helper():
            if vals[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = helper()
            node.right = helper()
            return node
        return helper()

            


        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))