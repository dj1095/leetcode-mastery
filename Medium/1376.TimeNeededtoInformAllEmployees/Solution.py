from collections import defaultdict, deque
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adj = defaultdict(list)
        for i in range(n):
            adj[manager[i]].append(i)
        max_time_taken = 0
        q = deque()
        q.append((headID, informTime[headID]))
        while q:
            empId, time  = q.popleft()
            max_time_taken = max(max_time_taken, time)
            for emp in adj[empId]:
                q.append((emp, time + informTime[emp]))
        return max_time_taken