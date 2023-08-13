class Solution:
    ####NOT Optimal
    #Time Complexity - O(N)
    #Space Complexity - O(N)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_size = len(nums)
        prefixProd = [1] * (nums_size)
        postfixProd = [1] * (nums_size)
        result = [1] * (nums_size)
        j = nums_size
        prefixProd[0] = 1
        for i in range(1,nums_size):
            prefixProd[i] = prefixProd[i - 1] * nums[i - 1]
        postfixProd[nums_size - 1] = 1
        for j in range(nums_size - 2, -1 ,-1):
            postfixProd[j] = postfixProd[j + 1] * nums[j + 1]
        for idx in range(nums_size):
            result[idx] = prefixProd[idx] * postfixProd[idx]

        return result

