class Solution:
    #Time Complexity - O(N)
    #Space Complexity - O(1)
    def longestOnes(self, nums: List[int], k: int) -> int:
        result = start = 0
        zeros_count = 0

        for end in range(len(nums)):
            if nums[end] == 0:
                zeros_count += 1

            while zeros_count > k:
                if nums[start] == 0:
                    zeros_count -= 1
                start += 1
            result = max(result, end - start + 1)
        return result