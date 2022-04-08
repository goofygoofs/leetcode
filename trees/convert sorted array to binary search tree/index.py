'''
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

 

Example 1:


Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:


Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in a strictly increasing order.
'''

'''
mid index create a node out of it

create function that takes in a TreeNode, the list?, and index?
'''

'''
given array where every number is in ascending order.
convert it to a height balanced BST. every subtree is never differ by 1
we can just do linked list but they want it to be a balanced search tree

[-10,-3,0,5,9]

noticed they chose 0 to be the root
why did we choose 0 as the middle?
that means the values on the left of it will go in the left subtree
and the values on the right of it will go in the right subtree
it's a recursive definition isn't it?
our job is to take this smaller sorted array and create a binary search tree with them
we can solve this problem easily using recursion

left pointer at the beginning and right pointer at the end
find the mid point, using our left and right pointers
remove the mid element because we create a node with it
next we need to create the left subtree with these elements for our root node

move the right pointer to the position to the right of the mid
does it matter if we choose -10 or -3 as or mid? it doesn't
let's choose -3 as our mid, it's gonna be the root
we don't have any more elements to the right for this subtree so we will
take our right pointer and shift it to the left and create a left subtree from this single element
left and right are together that means mid is in this position so the 
left child of -3 is -10. in reality our algo is going to have a different base case now
we're gonna continue for this -10 let's see if we can have a left subtree for it
we know there's not any elements over here but we're still going to try.
we try moving our right pointer over but now it is. so we end up returning None

we have another job and that's to create a right subtree for our root node
so with our right pointer still remaining at this value right our rightmost boundary and since mid was initially here
we're going to take a left pointer and put it over here
doesn't matter where the mid is because we have 2 element.
let's say mid is 9
there's no right to the right of 9
we have some left elemeents so we shift our right over to the left
mid is now 5 because left and right are both over 5
5 is less than 9 so it goes in the left 
this is one of the potential solution

we are given a single parameter of nums and we want
to return a tree node right so we're given a list we want to convert
it to a tree
we are going to create a helper function
pass in 2 parameters, left and right
left and right will tell us what portion of the input nums we're actually considering
so we don't have to pass the entire nums array into our helper function
this helper function is nested in our other function
our helper function will be recursive so the first thing we want to do is handle the base case
if left ever happens to be greater than right
that means we can return

time - O(n)
space - O(log(n)) height of our tree because we know our tree is going to be balanced.
'''

# Definition for a binary tree node.
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        # helper takes in index for nums. left and right are indexes
        def helper(l, r):
            if l > r:
                return None
            
            m = (l + r) // 2
            root = TreeNode(nums[m])
            # since this is the left subtree the left stays the same
            # the right is going to be mid - 1
            root.left = helper(l, m - 1)
            root.right = helper(m + 1, r)
            return root
        
        return helper(0, len(nums) - 1)