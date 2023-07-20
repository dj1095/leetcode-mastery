class Solution:
    def climbStairs(self, n: int) -> int:
        last = 1
        lastBefore = 1
        for i in range(n-1):
            temp = lastBefore
            lastBefore = lastBefore + last
            last = temp
        return lastBefore

            