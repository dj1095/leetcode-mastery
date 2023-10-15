class Solution:
    #Time Complexity - O(N)
    #Space Complexity - O(1)
    def singleNumber(self, nums: List[int]) -> int:
        result = nums[0]
        for i in range(1, len(nums)):
            #XOR results in 0 when perfromed on same number
            result ^= nums[i]
        return result
            