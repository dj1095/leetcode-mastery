class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #Top Down Approach with memoization
        #Time Complexity - O(S * N) given S is half of the total sum of elements
        #Space Complexity - O(S * N) 

        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        required_sum = int(total_sum / 2)
        
        dp = [[False for _ in range(required_sum + 1)] for _ in range(len(nums))]

        # zero is found for every subset
        for i in range(len(nums)):
            dp[i][0] = True
        
        #when we have only one element
        for s in range(1,required_sum + 1):
            dp[0][s] = dp[0][s] == nums[0]

        for i in range(1, len(nums)):
            for s in range(1,required_sum + 1):
                if nums[i] <= s:
                    dp[i][s] = (dp[i-1][s] or dp[i-1][s - nums[i]])
                else:
                    dp[i][s] = dp[i-1][s]
        return dp[len(nums) - 1][required_sum]

                

        