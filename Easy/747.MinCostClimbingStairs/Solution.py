class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #A Bottom Up DP Approach - [ Just like Climbing Stairs problem]
        #Time Complexity - O(N)
        #Space Complexity - O(1)
        first , last = 0,0
        for i in range(len(cost)-1, -1, -1):
            temp = first
            first = min(cost[i]+first, cost[i]+ last)
            last = temp
        return min(first, last)