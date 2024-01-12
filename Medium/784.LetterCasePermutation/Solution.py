class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        # Time Complexity - O(N * 2^K) where K is the total letters in str (not digits) and N is len(str)
        # Space Complexity - O(N * 2^K)
        perms = [[]]
        for chr in s:
            n = len(perms)
            for i in range(n):
                if chr.isalpha():
                    new_perm = list(perms[i])
                    new_perm.append(chr.swapcase())
                    perms.append(new_perm)
                perms[i].append(chr)

        return ["".join(p) for p in perms]
