'''
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 

Example 1:


Input: head = [1,2,3,4]
Output: [1,4,2,3]
Example 2:


Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
 

Constraints:

The number of nodes in the list is in the range [1, 5 * 104].
1 <= Node.val <= 1000
'''

'''
front and end pointers
create a stack and count variable to keep count using while loop while moving end pointer to the back
shift front pointer using next variable, and updating it's next to end
pop off end until correct amount of count variable

O(n) time
O(n) space for stack

'''

'''
we can do this without using an array and without using extra memory
we want to take the first half with the 2nd half with alternating value and 
the 2nd list starts at the end
one pointer starts at the beginning of the first list
and one pointer at the start (which is the end) of the 2nd list
the link is going the wrong way for the 2nd list
why not just reverse the links?
2 phases:
take 2nd portion of list and reverse it
then merge it together with the first list
when we're reversing 2nd half, how do we know we reach the 2nd half?
easiest way is to use a fast and slow pointer
we are goind to have the slow pointer at the 1st node
and fast pointer at 2nd node
we are shifting slow by 1 and fast by 2.
we stop when fast reaches the end of the list or None
slow is going to end at the end of the 1st half so we can say slow.next is the beginning of the 2nd list (even number of nodes)
what if we have an odd number of nodes?
then slow will be at the middle.
it works for us because that middle node will be the last node
for the last node in the first half of the list (odd number length), we don't want it to point at the 2nd half but at None

O(m + n) time
O(1) space
'''

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        # last node set to None
        prev = slow.next = None
        
        # reverse 2nd portion of the list
        while second:
            next = second.next
            second.next = prev
            prev = second
            second = next
        
        # merge two halfs
        first, second = head, prev
        while second: #2nd half less length than 1st half
            next1, next2 = first.next, second.next
            first.next = second
            second.next = next1
            # shift pointers
            first, second = next1, next2
        
        # don't need to return anything
        



