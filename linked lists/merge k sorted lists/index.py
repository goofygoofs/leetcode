"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
 

Constraints:

k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104
"""

"""

import heapq
heapify ( O(n) )− This function converts a regular list to a heap. In the resulting heap the smallest element gets pushed to the index position 0. But rest of the data elements are not necessarily sorted.
heappush ( O(log n) ) − This function adds an element to the heap without altering the current heap.
heappop ( O(log n) ) − This function returns the smallest data element from the heap.
heapreplace − This function replaces the smallest data element with a new value supplied in the function.





while len(lists) > 0:

pop all of them put it in a heap with tuple. (ListNode, index in lists)
pop off heap lowest value, replace with the next node in that list. if next node is None, remove from array. ie pop(index)
return newly merge list
"""

# Definition for singly-linked list.
from typing import Optional, List
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __lt__(self, other):
      return self.val < other.val


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 1 and lists[0] is None:
            return None

        dummy = ListNode(0)
        curr = dummy
        heap = []

        for i in range(0, len(lists)):  # O( len(lists)log(len(list)) )
            if lists[i] is None:
                continue
            # change all lists into queues
            node = lists[i]
            # heappush into heap, the popped left item from the list
            heapq.heappush(heap, (ListNode(node.val), node, i))

        while len(heap) > 0: # (nlogk) n is total number of nodes combined. k is total number of nodes in largest node
            _, node, i = heapq.heappop(heap)
            if node.next:
                heapq.heappush(heap, (ListNode(node.next.val), node.next, i))
            curr.next = node
            curr = node

        return dummy.next
