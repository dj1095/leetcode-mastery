class Solution:
    # Time complexity - O(N)
    # Space COmplexity - O(N)

    # Using dictionary
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        map = {}
        for i in range(len(nums)):
            if nums[i] in map and i - map[nums[i]] <= k:
                return True
            map[nums[i]] = i
        return False
