class Solution:
    #Time Complexity - O(N)
    #Space Complexity - O(1)
    def longestSubarray(self, nums: List[int]) -> int:
        start = 0 
        result = 0
        consecutive_1s = 0
        for end in range(len(nums)):
            if nums[end] == 1:
                consecutive_1s += 1
            if (end - start + 1) - consecutive_1s > 1:
                if nums[start] == 1:
                    consecutive_1s -= 1
                start += 1
            result = max(result , end - start)
        return result 
            
        