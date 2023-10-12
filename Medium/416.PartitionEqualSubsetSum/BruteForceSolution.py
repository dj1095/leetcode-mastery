class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #Brute Force Algo
        #Trying out all the posssibilities
        #Time Complexity - O(2^N)
        #Space Complexity - O(N) because we can atmost have N recursive calls on stack at any time

        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        
        #Recursive Function
        def can_partition_recursive(current_sum , current_idx):
            if current_sum == 0:
                return True
            if current_idx >= len(nums):
                return False
            if nums[current_idx] <= current_sum:
                if can_partition_recursive(current_sum - nums[current_idx] , current_idx + 1):
                    return True
            return can_partition_recursive(current_sum, current_idx + 1)
        return can_partition_recursive(total_sum/2 , 0)