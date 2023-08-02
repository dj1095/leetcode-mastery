class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left , total = 0, 0
        minLen = float("inf")
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                minLen = min(minLen, r - left + 1)
                total -= nums[left]
                left += 1

        return 0 if minLen == float("inf") else minLen
