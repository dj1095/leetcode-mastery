class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Time Complexity - O(N)
        #Space Complexity - O(1)
        left, right = 0, len(nums) - 1
        i =0
        while i <= right:
            if nums[i] == 0:
                nums[left], nums[i] = nums[i] , nums[left]
                left += 1
            elif nums[i] == 2:
                nums[right] , nums[i] = nums[i], nums[right]
                right -= 1
                i -= 1 # to keep i at the same level when doing right swap 
            i += 1
        return nums
            