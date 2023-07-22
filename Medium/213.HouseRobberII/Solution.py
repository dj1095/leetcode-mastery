class Solution:
    def rob(self, nums: List[int]) -> int:

        def helper(num_arr):
            rob1 = rob2 = 0

            for n in num_arr:
                max_amt = max(rob1+n, rob2)
                rob1 = rob2
                rob2 = max_amt
            return rob2
        return max(nums[0],helper(nums[:-1]), helper(nums[1:]))
