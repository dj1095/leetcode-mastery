#Time Complexity - O(N)
#Space Complexity - O(1)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum  = 0
        maxSum = float("-inf")
        for i in range(len(nums)):
            currSum = max(currSum + nums[i], nums[i])
            maxSum = max(maxSum, currSum)
        return maxSum
