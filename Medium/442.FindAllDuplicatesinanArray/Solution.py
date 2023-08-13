class Solution:
    #Time Complexity - O(N)
    #Space Complexity - O(1)
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = []
        for i in range(len(nums)):
            idx = abs(abs(nums[i]) - 1)
            if nums[idx] < 0:
                duplicates.append(idx + 1)
            else:
                nums[idx] *= -1
        return duplicates
