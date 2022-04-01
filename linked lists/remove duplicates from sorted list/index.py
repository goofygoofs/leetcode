'''
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

 

Example 1:


Input: head = [1,1,2]
Output: [1,2]
Example 2:


Input: head = [1,1,2,3,3]
Output: [1,2,3]
 

Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
'''

'''
return base case if no linked list

can't loop, so create we need to check previous value. if next value is None... return 
create start can add it's next to head. return start at the end
start -> head -> next
need previous too
             delete curr, update head to next
start -> 2 -> 2 -> 2 -> 4
             prev next
                  head

'''

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        start = ListNode()
        start.next = head

        prev = head
        next = None

        if head.next is not None:
            head = head.next
            next = head.next
            # duplicate
            if head.val == prev.val:
                head.next = None
                prev.next = head
            head = next
            prev = head
        return start.next

sol = Solution()

output = sol.deleteDuplicates(head = [1,1,2])
print(output)