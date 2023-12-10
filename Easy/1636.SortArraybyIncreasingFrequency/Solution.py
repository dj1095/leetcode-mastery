class Solution:
    # Time Complexity - O(N * logN)
    # Space Complexity - O(1)
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1
        nums.sort(key=lambda x: (freq[x], -x))
        return nums
