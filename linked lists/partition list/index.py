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

'''
partition list that every value less than x is on the left side, and greater or equal on the right side
preserve the original order 

O(n) time
O(1) space

make 2 different sublist
all less than values in the left list
all greater than or equal in the requal
take the left list and connect it to the beginning of the right list
x=3
1->4->3->2->5->2
left->1->2->2->None
right->4->3->5->(connected to the 2)

take 2 at end of left connect it to beginning of right 4
take the 5 and change it's next to None

it's O(1) space because we are just using head and storing that to a variable?

'''

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # dummy nodes
        left, right = ListNode(), ListNode()
        # will always point at the last node in our left and right list
        # so we can easily add an element to the end of these lists
        ltail, rtail = left, right

        while head:
            if head.val < x:
                ltail.next = head
                ltail = ltail.next
            else:
                rtail.next = head
                rtail = rtail.next
            head = head.next
        
        # we do right.next because right itself is a dummy node
        ltail.next = right.next
        # need to terminate list and have it point at None
        rtail.next = None
        return left.next