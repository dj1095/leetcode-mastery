class Solution:
    #Time Complexity - O(N * S) where S is length of required sum array
    #Space Complexity - O(S)
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)
        if total_sum < abs(target) or  (target + total_sum )%2 == 1:
            return 0
        #Some math before that 
        #sum(s1) - sum(s2) = target
        #sum(s1) - sum(s2) = sum(nums)
        required_target = int((target + total_sum)/2)
        #Space Optimized Dp Array
        dp = [0 for _ in range(required_target + 1)]
        #We can always form a sum 0 subset
        dp[0] = 1

        for i in range(len(nums)):
            for s in range(required_target , -1 , -1):
                if s >= nums[i]:
                    dp[s] += dp[s - nums[i]]
        return dp[required_target]
            