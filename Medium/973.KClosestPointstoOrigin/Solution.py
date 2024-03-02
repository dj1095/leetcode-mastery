from heapq import *
from math import *


class Solution:
    # Time Complexity - O(N * logK)
    # Space Complexity - O(K)
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result = []
        heap = []
        for point in points:
            distance = self.calc_euclidean_dist_from_origin(point)
            heappush(heap, (-distance, point))
            if len(heap) > k:
                heappop(heap)

        while heap:
            _, point = heappop(heap)
            result.append(point)
        return result

    def calc_euclidean_dist_from_origin(self, point):
        return (point[0] ** 2) + (point[1] ** 2)
