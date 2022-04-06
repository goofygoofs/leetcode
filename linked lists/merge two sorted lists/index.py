'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
'''

'''
pointer on each list

we gonna compare and create a new node of the lowest value, iterate one for the used value
if one list is None go out of loop and add the rest of the other list

time - O(n + m)
space - O(n + m)
'''

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        mergedList = ListNode(-1) 
        curr = mergedList

        while list1 and list2:
            if list1.val <= list2.val:
                node = ListNode(list1.val)
                curr.next = node
                curr = node
                list1 = list1.next
            else:
                node = ListNode(list2.val)
                curr.next = node
                curr = node
                list2 = list2.next
        
        while list1:
            node = ListNode(list1.val)
            curr.next = node
            curr = node
            list1 = list1.next
        
        while list2:
            node = ListNode(list2.val)
            curr.next = node
            curr = node
            list2 = list2.next

        return mergedList.next
