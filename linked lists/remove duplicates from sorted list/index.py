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

'''
when they say list they actually mean a linked list and this mean in this case removing values
from a linked list is done with pointers. take this link here and link it to the next one. we are not 
paying attention to deleting the node. 
1->1->2
we can remove either 1's, it doesn't matter which one.
it makes sense to maintain the order and when we're done return the head

usually when we start we have a dummy node. it's not really necessary because the head is never going to change
best way of handling is never removing the head. remove the extra 1's coming after it. guarantees the head never gets deleted
dummy comes in handy if head gets deleted. good thing about dummy is that it always points to the head. 
but in this case we don't need dummy node

    1 -> 1 -> 1 -> 3 -> 3
   curr

    1 -> 1 -> 3 -> 3

    1 -> 3 -> 3

    1 -> 3


we're going to have current point at whatever the current node happens to be and of course
initially it's going to be at the head of the linked list and we know that the list is sorted
so of course duplicates are going to be right next to each other
so the question now is ths is the current node is the next node right after it is it a duplicate
is it the same as the current node?
in this case yes it is. we need to remove this duplicat. since this is curr, the duplicate is curr.next
we need to take this pointer and point it to the next node.
curr.ext = curr.next.next
basically what we did is take this node and point at the next.next node which deleted the duplicate from the linked list

curr still stays at the same position because the next one can still be a duplicate. so we do it again and now curr.next will be 3

it's not the same value so we can shift over current now.

so when current is 3, the next is None. so we move curr over and when curr is None, we are ddone

time complexity is O(n)
space is O(1)

the way we are implementing this is a nested loop
loop1
    loop2 (nested loop)

just because we have nested loop doesnt mean it's n^2
outer loop (loop 1) determines where our current pointer is.
the inner loop deleted the node inbetween, takes care of the duplicate. 
outer loop takes care of the unique value nodes.
'''

# Definition for singly-linked list.
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        
        # keep doing this loop until we hit None
        while cur:
            # inner loop handles deleting
            # if they are the same value
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next
            # when it finds the next unique val, update cur
            cur = cur.next

        return head
    
    def generateLinkedList(self, arr: Optional[ListNode]) -> Optional[ListNode]:
        if len(arr) == 0:
            return None
        head = ListNode(arr[0])
        tail = head
        if len(arr) == 1:
            return head

        i = 1

        while i < len(arr):
            tail.next = ListNode(arr[i])
            tail = tail.next
            i += 1
        
        return head



sol = Solution()

node = sol.generateLinkedList([1,1,2])
output = sol.deleteDuplicates(node)
print(output.val, output.next.val)