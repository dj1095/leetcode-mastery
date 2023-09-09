import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        #Time Complexity - O(K * NlogN)
        #Space Complexity - O(N)
        min_cap_heap = []
        max_profit_heap = []
        available_cap = w

        for i in range(len(capital)):
            heappush(min_cap_heap, (capital[i] , i))

        for _ in range(k):
            while min_cap_heap and min_cap_heap[0][0] <= available_cap:
                cap , pos = heappop(min_cap_heap)
                heappush(max_profit_heap, (-profits[pos] , pos))
            if not max_profit_heap:
                break
            available_cap += (-heappop(max_profit_heap)[0])

        return available_cap



        