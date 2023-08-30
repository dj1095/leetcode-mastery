class Solution:
    def jump(self, nums: List[int]) -> int:
        #Time Complexity - O(N)
        #Space Complexity - O(1)
        goal = len(nums) - 1
        left = right = 0
        number_of_jumps = farthest = 0
        while right < goal:
            for i in range(left,right + 1):
                farthest = max(farthest, i + nums[i])
            left = right + 1
            right = farthest
            number_of_jumps += 1
        return number_of_jumps

            
