from collections import defaultdict
from heapq import *


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        # finding the frequencies of the nums
        freq_map = defaultdict(int)
        for num in nums:
            freq_map[num] += 1
        # Build a heap of freq_map array
        heap = []
        for num, freq in freq_map.items():
            heappush(heap, (freq, num))
            if len(heap) > k:
                heappop(heap)

        # Access top K frequent Elements
        while heap:
            result.append(heappop(heap)[1])

        return result
