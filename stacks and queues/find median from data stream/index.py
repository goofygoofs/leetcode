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

gotta use a minQueue and maxQueue to find median.

#  two heaps, large, small, minheap, maxheap
# heap should be equal size

for maxHeap (small), multiply the number by -1 before adding in
'''

'''
median is the middle value, if list is even there is no middle value, so we take the sum and divide by 2 (if odd)
we are going to have 2 subsets and all all elements on the left is goingg to be length less than or equal all elements in the right 

[small heap] = [large heap]
[3 elements] = [2 elements] ok
if more than 1 element, we have to balance it so it's even or off by 1

add/remove is log(n)

maxHeap - find max is O(1). implemented as a maxHeap

minHeap - find min is O(1). implemented as a minHeap

small heap (max heap) [1,2] -> need 2

large heap (min heap) [3, 4] -> need 3

will only work if length is the same or off by 1

if odd number of elements, we want to get the max value from the maxHeap

maxHeap - [1,2,3]
minHeap - [4,5]

add/remove from heap is O(log(n)) operation

finding max/min from max/min heap is O(1) operation

last condition is is all elements in maxHeap(small) less than in minHeap(large)?
small heap [maxHeap] [2, 7]
large heap [minHeap] [3]

the answer is no. remove the 7 and add it to min heap

so it is [maxHeap] [2]
[minHeap] [7, 3]

how about if we add 4?

[2, 4]

[7, 3]

=>

[2]

[7, 4, 3]

pop 4 and add to minHeap but no the length aren't equal or off by 1
what do we do?

find min from minHeap, popoff and add to maxHeap

[2, 3]

[7, 4]

time complexity of .getMedian is O(1)

time complexity of .addNum is O(log(n))

'''
import heapq
class MedianFinder:

    def __init__(self):
        #  two heaps, large, small, minheap, maxheap
        # heap should be equal size
        self.small, self.large = [], [] # maxHeap, minHeap (python default)

    def addNum(self, num: int) -> None:
        # always add to small
        # in python only implements min heaps, we know small is actually a maxHeap
        # so to get around that we are going to multiply by -1
        heapq.heappush(self.small, -1 * num)

        # make sure every num small is <= every num in large
        # also balance length - difference greater than 1?
        if (self.small and self.large and (-1 * self.small[0]) > self.large[0]) \
        or len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        # also balance length from vice/versa 
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        # odd length and more small than large
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        # odd length and more large than small
        elif len(self.large) > len(self.small):
            return self.large[0]
        #  even length
        return (-1 * self.small[0] + self.large[0]) / 2



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()