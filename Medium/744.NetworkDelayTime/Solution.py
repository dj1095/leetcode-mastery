from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for src,dest,dist in times:
            adj[src].append((dest,dist))

        minheap = [(0,k)]
        total_distance = 0
        visit = set()
        while minheap:
            dist, node = heapq.heappop(minheap)
            if node in visit:
                continue
            visit.add(node)
            total_distance = max(total_distance, dist)
            for dest2, dist2 in adj[node]:
                if dest2 not in visit:
                    heapq.heappush(minheap, (dist+dist2, dest2))
        return total_distance if len(visit) == n else -1
                