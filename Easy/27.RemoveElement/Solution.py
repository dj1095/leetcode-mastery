class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        '''
        Space Complexity - O(1)
        Time Complexity - O(N) where N is total number of elements in the nums array
        '''
        i = 0
        j = len(nums) - 1
        while i <= j:
            if nums[j] == val:
                j -= 1
            elif nums[i] == val:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
            else:
                i += 1
        return i
            

