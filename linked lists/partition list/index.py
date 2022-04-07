'''
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

 

Example 1:


Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
Example 2:

Input: head = [2,1], x = 2
Output: [1,2]
 

Constraints:

The number of nodes in the list is in the range [0, 200].
-100 <= Node.val <= 100
-200 <= x <= 200
'''

'''
2 pointers: left and right
left will always stay at lower than x position right before higher than x, ready to take in the next node
right will iterate through and check if the next exists and if does whether to update it's next position based on lower than x
right.next = right.next.next, if exists
also case to check if at end

also check if list starts off with >= x value
update pointers check if starting is >= x 
update head too
move right most to x >= x so the next will be leftNext
and check if left exists (all elements >= x)
what if all elements < x?
update right to be at least furthest element < x
'''

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head is None:
            return None
        
        if head.next is None:
            return head
        
        left = head
        right = head

        leftMostGreaterThanX = False

        # starting left
        while left:
            if left.val < x:
                break
            leftMostGreaterThanX = True
            left = left.next
        
        # update pointers 
        if leftMostGreaterThanX:
            leftNext = left.next
            left.next = right
            # move right to right most:
            while right.next.val >= x:
                right = right.next
            right.next = leftNext
            right = right.next
            head = left

        while right:
            if right.next:
                if right.next.val < x:
                    next = left.next
                    left.next = right.next
                    left = left.next
                    if right.next.next:
                        right.next = right.next.next
                    else:
                        right.next = None
                        right = None
                    left.next = next
                else:
                    right = right.next
        
        return head
            