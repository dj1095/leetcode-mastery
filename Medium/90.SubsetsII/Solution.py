class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Time Complexity - O(N * 2^N)
        # Space Complexity - O(N * 2^N)
        # sort nums to arrange duplicates next to each other
        nums.sort()

        subsets = [[]]
        endIdx = 0
        for idx in range(len(nums)):
            startIdx = 0
            # if duplicate found then only consider subsets from previous iterations
            if idx > 0 and nums[idx] == nums[idx - 1]:
                startIdx = endIdx + 1
            endIdx = len(subsets) - 1
            for i in range(startIdx, endIdx + 1):
                sub1 = list(subsets[i])
                sub1.append(nums[idx])
                subsets.append(sub1)
        return subsets
