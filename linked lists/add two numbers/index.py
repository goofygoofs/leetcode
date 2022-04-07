'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
'''

'''
go to the end of both list
create a new list adding
carry over if >= 10
also if remainder without carry over, then add the extra digit
keep count variables for both for leading zero and add leading zero when adding
can do in 1 loop  with or statement and if reach end of prevl1 or prevl2, keep adding zeros

time - O(max(n, m))
space - O(max(n, m)) to create summed list

'''

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        currl1 = l1
        prevl1 = None
        currl2 = l2
        prevl2 = None
        
        remainder = 0
        dummy = ListNode(-1)
        curr = dummy

        while currl1 or currl2:
            if currl1:
                next = currl1.next
                currl1.next = prevl1
                prevl1 = currl1
                currl1 = next
            else:
                next = ListNode(0)
                prev = prevl1
                prevl1 = next
                prevl1.next = prev
            if currl2:
                next = currl2.next
                currl2.next = prevl2
                prevl2 = currl2
                currl2 = next
            else:
                next = ListNode(0)
                prev = prevl2
                prevl2 = next
                prevl2.next = prev
        
            val = prevl1.val + prevl2.val + remainder

            if val >= 10:
                remainder = 1
                val = val % 10
            else:
                remainder = 0

            node = ListNode(val)
            curr.next = node
            curr = curr.next            
        
        if remainder > 0:
            node = ListNode(remainder)
            curr.next = node
            curr = node


        return dummy.next

