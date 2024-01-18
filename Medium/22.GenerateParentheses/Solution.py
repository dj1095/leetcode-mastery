from collections import deque


class GPS:
    def __init__(self, parentheses, openCount, closeCount):
        self.parentheses = parentheses
        self.openCount = openCount
        self.closeCount = closeCount


class Solution:
    # Time Complexity - O(2^N * N)
    # Space Complexity - O(2^N * N)
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        q = deque()
        q.append(GPS("", 0, 0))
        while q:
            ps = q.popleft()
            if ps.openCount == n and ps.closeCount == n:
                result.append(ps.parentheses)
            else:
                if ps.openCount < n:
                    ips1 = GPS(ps.parentheses +
                               "(", ps.openCount + 1, ps.closeCount)
                    q.append(ips1)
                if ps.closeCount < ps.openCount:
                    ips2 = GPS(ps.parentheses + ")",
                               ps.openCount, ps.closeCount + 1)
                    q.append(ips2)
        return result
