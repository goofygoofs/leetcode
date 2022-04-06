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
        # create stack and count variable
        # length of node CAN be 1... review
        stack = []
        count = 0
        curr = head
        end = None
        while curr:
            count += 1
            stack.append(curr)
            curr = curr.next
        
        if count == 1:
            return head

        front = head
        while count > 0:
            next = front.next
            end = stack.pop()
            # print('end.val', end.val)
            if count == 1: # odd length count
                front.next = None
                return head
            front.next = end
            if next == end: # even length count
                end.next = None
                return head
            end.next = next
            front = next
            count -= 2
        
        return head
