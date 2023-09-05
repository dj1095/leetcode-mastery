import heapq
from heapq import *


class Solution:
    #Time Complexity - O(N*k)
    #Space Complexity - O(k)
    def medianSlidingWindow(self, nums, k: int):
        result = [0 for i in range(len(nums) - k + 1)]
        minHeap  = []
        maxHeap = []

        def rebalance():
            if len(maxHeap) > len(minHeap) + 1:
                heappush(minHeap, -heappop(maxHeap))
            elif len(maxHeap) < len(minHeap):
                heappush(maxHeap, -heappop(minHeap))

        def deleteElement(heap, element):
            idx = heap.index(element)
            heap[idx] = heap[-1]
            heap.pop()
            if idx < len(heap):
                heapq._siftup(heap, idx)
                heapq._siftdown(heap, 0, idx)

        for i in range(len(nums)):
            ## Heap Insertion
            if not maxHeap or -maxHeap[0] > nums[i]:
                heappush(maxHeap, -nums[i])
            else:
                heappush(minHeap, nums[i])

            # Rebalance Heaps
            rebalance()

            # Heap Maintaining window size k
            if i - k + 1 >= 0:
                if len(maxHeap) == len(minHeap):
                    result[i - k + 1] = (minHeap[0] + (-maxHeap[0])) / 2.0
                else:
                    result[i - k + 1] = -maxHeap[0] / 1.0

                # move Window forward
                elementToBeRemoved = nums[i - k + 1]
                if elementToBeRemoved <= -maxHeap[0]:
                    deleteElement(maxHeap, -elementToBeRemoved)
                else:
                    deleteElement(minHeap, elementToBeRemoved)
                rebalance()
        return result
