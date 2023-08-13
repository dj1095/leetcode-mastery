class Solution:
    ####Optimal (Two Passes)
    #Time Complexity - O(N)
    #Space Complexity - O(1)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * (len(nums))
        prefix = postfix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        for j in range(len(nums) - 1, -1, -1):
            result[j] *= postfix
            postfix *= nums[j]
        return result


