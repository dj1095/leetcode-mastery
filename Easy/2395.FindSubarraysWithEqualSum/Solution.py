class Solution:
    #Time Complexity - O(N)
    #Space Complexity - O(N)
    def findSubarrays(self, nums: List[int]) -> bool:
        sums = set()
        for i in range(len(nums) - 1):
            j = i+1
            if nums[i] + nums[j] in sums:
                return True
            sums.add(nums[i] + nums[j])
        return False