class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #Time Complexity - O(logN)
        #Space Complexity - O(1)
        def b_search(left, right, key):
            while left <= right:
                mid = left + ((right - left)//2)
                if nums[mid] == key:
                    return mid
                elif nums[mid] > key:
                    right = mid - 1
                else:
                    left = mid + 1
            return left
        return b_search(0, len(nums) - 1, target)
            


