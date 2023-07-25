from collections import defaultdict
import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Get Adj list of the graph
        flightConnections = defaultdict(list)
        for frm,to,price in flights:
            flightConnections[frm].append((price,to))
        
        maxCityHops={}
        #Intial state of heap (price, k, dest)
        minheap = [(0,0,src)]
        while minheap:
            currentPrice, numOfStops, node = heapq.heappop(minheap)
            maxCityHops[node] = numOfStops
            if node == dst:
                    return currentPrice 
            if numOfStops > k:
                continue
            for connPrice, connNode in flightConnections[node]:
                if connNode in maxCityHops and maxCityHops[connNode] <= numOfStops:
                    continue
                heapq.heappush(minheap,(currentPrice + connPrice, numOfStops + 1, connNode))
        return -1 
            

                






        
