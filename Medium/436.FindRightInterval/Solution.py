import heapq
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        max_start_heap = [(-intervals[i][0] , i) for i in range(len(intervals))]
        max_end_heap = [(-intervals[i][1] , i) for i in range(len(intervals))]
        result = [-1 for i in range(len(intervals))]
        heapify(max_start_heap)
        heapify(max_end_heap)
            
        for i in range(len(intervals)):
            top_end , end_idx = heappop(max_end_heap)

            if -top_end <= -max_start_heap[0][0]:
                top_start, start_idx = heappop(max_start_heap)
                while max_start_heap and -top_end <= -max_start_heap[0][0]:
                    top_start, start_idx = heappop(max_start_heap)
                result[end_idx] = start_idx
                heappush(max_start_heap, (top_start, start_idx))

        return result