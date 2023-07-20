class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        idxToReplace = 1
        previousNum = nums[0]
        for i in range(1,len(nums)):
            if nums[i] != previousNum:
                nums[idxToReplace] = nums[i]
                idxToReplace += 1
                previousNum = nums[i]
        return idxToReplace
           
            
