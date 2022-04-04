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

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        linkedlist = self.createListNode([1,2,2])
        left = head
        right = head
        index = 0

        # iterate right until the end
        while right.next:
            prev = right
            right = right.next
            right.prev = prev
            index += 1
        
        while index > 0: # 1 -> 2 -> 2 -> 1
            # print('index', index)
            if left.val != right.val:
                return False
            left = left.next
            right = right.prev
            index -= 2
        
        return True

    def createListNode(self, arr: list[int]) -> Optional[ListNode]:
        head = ListNode(arr[0])
        curr = head

        for i in range(1, len(arr)):
            node = ListNode(arr[i])
            prev = curr
            curr.next = node
            curr = node
            curr.prev = prev
        
        return head

# sol = Solution()

# linkedlist = sol.createListNode([1,2,2])
# print(linkedlist.val, linkedlist.next.val, linkedlist.next.next.val)
# output = sol.isPalindrome(linkedlist)
# print(output)
