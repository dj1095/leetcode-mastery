class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # This is in Cyclic Sort Pattern
        #Approach : Place the elements in their indices - elments ignore elements > length of array
        ####### Search for the smallest missing positive numver 
        #Time Complexity - O(N)
        #Space Complexity - O(1)

        currentIdx = 0
        while currentIdx < len(nums):
            if nums[currentIdx] <= 0 or nums[currentIdx] > len(nums):
                currentIdx += 1
                continue
            # Ignoring 0 as element and considering like 1 -indexed array 
            currentElementIdx = nums[currentIdx] - 1 
            # Check if the element is at the correct position
            if nums[currentIdx] != nums[currentElementIdx]:
                nums[currentIdx] , nums[currentElementIdx] = nums[currentElementIdx] ,  nums[currentIdx]
            else:
                currentIdx += 1
        
        # Search for smallest missing positive number
        for i in range(len(nums)):
            if i + 1 != nums[i]:
                return i + 1
        return len(nums) + 1

        