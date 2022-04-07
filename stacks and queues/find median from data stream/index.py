'''
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
 

Example 1:

Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
 

Constraints:

-105 <= num <= 105
There will be at least one element in the data structure before calling findMedian.
At most 5 * 104 calls will be made to addNum and findMedian.
 

Follow up:

If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
'''

'''
have 2 queues
when len of 1st queue larger, return the median (middle element). when it's even, popleft of the 2nd queue, add to first appendleft queue. also if even, return the median (q1[0] + q2[0])/2

append():- This function is used to insert the value in its argument to the right end of the deque.
appendleft():- This function is used to insert the value in its argument to the left end of the deque.
pop():- This function is used to delete an argument from the right end of the deque.
popleft():- This function is used to delete an argument from the left end of the deque.
'''
from collections import deque
class MedianFinder:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def addNum(self, num: int) -> None:
        if len(self.q1) != len(self.q2):
            # moves so it's even length
            self.move()
        self.q2.append(num)

    def findMedian(self) -> float:
        if len(self.q1) != len(self.q2):
            return self.q2[0]
        return (self.q1[0] + self.q2[0]) / 2.0

    def move(self) -> None:
        self.q1.appendleft(self.q2.popleft())



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()