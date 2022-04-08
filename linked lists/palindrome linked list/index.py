'''
Given the head of a singly linked list, return true if it is a palindrome.

 

Example 1:


Input: head = [1,2,2,1]
Output: true
Example 2:


Input: head = [1,2]
Output: false
 

Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9
 

Follow up: Could you do it in O(n) time and O(1) space?
'''

'''
palindrome - read the same front vs back

number of nodes is at least 1

have 2 pointers, left and right
iterate right until end
iterate until pointers cross. if values not equal return False, else return True
need a index variable to keep count
'''

'''
there's a technique: two pointers
one pointer is going to be fast
one pointer is going to be slow
why are we doing it like this?
the main idea is if both pointers start at the beginning and let's say our slow pointer moves one spot ahead
and our fast pointer moves two spots ahead
then when that's the case when our fast pointer reaches the end of the list
our slow pointer should be somewhere near the middle right
and so this is the idea we already know 
how to get to the beginning of the list right
we can basically check the beginning and the end and keep doing that and check if it's a palindrome
the only problem to these pointers is that they only go in one direction.
there's an algo to reverse a linked list
and that's exactly what we can do
starting from the middle, we can reverse the linked list
then it's easy to check if it's a palindrome or not
again we can do this in constant memory
we do have to update our data structure though
but we don't need an extra array or anything
'''

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head

        # keep going until fast is at the last node or reach None
        # find middle (slow)
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # reverse second half
        prev = None
        while slow:
            next = slow.next
            slow.next = prev
            prev = slow
            slow = next
        
        # check palindrome
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
        



# sol = Solution()

# linkedlist = sol.createListNode([1,2,2])
# print(linkedlist.val, linkedlist.next.val, linkedlist.next.next.val)
# output = sol.isPalindrome(linkedlist)
# print(output)
