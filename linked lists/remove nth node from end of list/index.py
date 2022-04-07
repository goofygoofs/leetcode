'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
 

Follow up: Could you do this in one pass?
'''

'''
2 pointers: start and end
initially create a distance n between start and end

while loop until end reaches the end
start.next = start.next.next
return head

end cases for 1 element and 2 elements in list
'''

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        start = head
        end = head

        for _ in range(n):
            end = end.next
        
        # n = length of list
        if end is None:
            # 2 items in list
            if start.next:
                return head.next
            # return None if remove only item in list
            else:
                return None
        
        while end.next:
            end = end.next
            start = start.next
        
        # at the end now remove nth node
        start.next = start.next.next
        return head
