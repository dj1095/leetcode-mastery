class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Time Complexity - O(N * 2^N)
        # Space Complexity - O(N * 2^N)
        subset_list = [[]]

        for currentNumber in nums:
            n = len(subset_list)
            for i in range(n):
                set1 = list(subset_list[i])
                set1.append(currentNumber)
                subset_list.append(set1)
        return subset_list
