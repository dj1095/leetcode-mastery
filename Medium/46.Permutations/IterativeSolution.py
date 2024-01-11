class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Iterative way
        # Time Complexity - O(N * N!)
        # Space Complexity - O(N * N!)
        nums_len = len(nums)
        permutations = deque()
        permutations.append([])
        result = []
        for current_num in nums:
            n = len(permutations)
            for perms in range(n):
                old_perm = permutations.popleft()
                for i in range(len(old_perm) + 1):
                    new_perm = list(old_perm)
                    new_perm.insert(i, current_num)
                    if len(new_perm) == nums_len:
                        result.append(new_perm)
                    else:
                        permutations.append(new_perm)
        return result
