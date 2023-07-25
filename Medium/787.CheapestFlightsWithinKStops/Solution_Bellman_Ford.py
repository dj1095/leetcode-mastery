class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Using Bellman-Ford - Time - O(E.k)
        #Space O(E.k)

        prices = [float("inf")] * (n)
        prices[src] = 0
        for _ in range(k + 1):
            temp = prices.copy()
            for source,destination,currentPrice in flights:
                if prices[source] == float("inf"):
                    continue
                if prices[source] + currentPrice < temp[destination]:
                    temp[destination] = prices[source] + currentPrice
            prices = temp
        return -1 if prices[dst] == float("inf") else prices[dst] 
            