class Solution:
    #Time Complexity - O(N)
    #Space Complexity - O(1)
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        start = 0
        product = 1
        result = 0
        for end in range(len(nums)):
            product *= nums[end]
            while product >= k and start <= end:
                product /= nums[start]
                start += 1
            result += end - start + 1
        return result

        