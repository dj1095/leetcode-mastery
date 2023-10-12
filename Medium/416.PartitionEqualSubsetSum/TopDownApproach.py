class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #Top Down Approach with memoization
        #Time Complexity - O(S * N) given S is half of the total sum of elements
        #Space Complexity - O(S * N) 

        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False

        #memoization Array
        dp = [[-1 for _ in range(int(total_sum / 2) + 1)] for _ in range(len(nums))]

        #Recursive Function
        def can_partition_recursive(current_sum , current_idx):
            if current_sum == 0:
                return 1
            if current_idx >= len(nums):
                return 0
            if dp[current_idx][current_sum] == -1:
                if (nums[current_idx] <= current_sum 
                        and can_partition_recursive(current_sum - nums[current_idx] , current_idx + 1) == 1):
                        dp[current_idx][current_sum] = 1
                        return 1
                dp[current_idx][current_sum] =  can_partition_recursive(current_sum, current_idx + 1)
            return dp[current_idx][current_sum] 

        return True if can_partition_recursive(int(total_sum/2) , 0) == 1 else False