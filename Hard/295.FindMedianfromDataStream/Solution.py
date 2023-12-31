from heapq import *
class MedianFinder:
    # Time Complexity - O(Log N ) for insertions , if N insertions then N * LOG N
    # Space Complexity - O(N) considering at any time we hold n elements in heaps

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []
        

    def addNum(self, num: int) -> None:
        if not self.maxHeap or -self.maxHeap[0] > num:
            heappush(self.maxHeap, -num)
        else:
            heappush(self.minHeap, num)
        ##Balance the heaps 
        if len(self.maxHeap) > len(self.minHeap) + 1:
            heappush(self.minHeap, -heappop(self.maxHeap))
        elif len(self.maxHeap) < len(self.minHeap):
            heappush(self.maxHeap , -heappop(self.minHeap))
        

    def findMedian(self) -> float:
        if (len(self.maxHeap) + len(self.minHeap)) % 2 == 0:
            return ((-self.maxHeap[0]) + (self.minHeap[0])) / 2.0
        return -self.maxHeap[0] / 1.0

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()