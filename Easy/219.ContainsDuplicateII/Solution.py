class Solution:
    # Time complexity - O(N)
    # Space COmplexity - O(K) K is the number of elements in the window , in the worst case it can be N
    # Sliding window technique
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        start, end = 0, 0
        store = set()
        while end < len(nums):
            if end - start > k:
                store.remove(nums[start])
                start += 1
            if nums[end] in store:
                return True
            store.add(nums[end])
            end += 1
        return False
