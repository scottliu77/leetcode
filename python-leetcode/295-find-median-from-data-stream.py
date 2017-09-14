'''

Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

Examples:

[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
For example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2
Credits:
Special thanks to @Louis1992 for adding this problem and creating all test cases.

'''


from heapq import *

class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minHeap = []
        self.maxHeap = []
        
    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if len(self.minHeap) == len(self.maxHeap):
            heappush(self.maxHeap, -heappushpop(self.minHeap, -num))
        else:
            heappush(self.minHeap, -heappushpop(self.maxHeap, num))   

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.maxHeap) == len(self.minHeap):
            return float(self.maxHeap[0] - self.minHeap[0]) / 2.0
        return float(self.maxHeap[0])

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()