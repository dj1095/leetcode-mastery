class Solution:
    # Top Down Approach
    # Time Complexity - O(N^2)
    # Space Complexity - O(N ^2) + O(N) for recursion =~ O(N^2)
    def longestPalindromeSubseq(self, s: str) -> int:
        # Initialiazing DP Array
        dp = [[-1 for _ in range(len(s))] for _ in range(len(s))]

        def lps_recursive(startIdx, endIdx):
            if startIdx > endIdx:
                return 0
            elif startIdx == endIdx:
                return 1
            if dp[startIdx][endIdx] == -1:
                if s[startIdx] == s[endIdx]:
                    dp[startIdx][endIdx] = 2 + \
                        lps_recursive(startIdx + 1, endIdx - 1)
                else:
                    c1 = lps_recursive(startIdx + 1, endIdx)
                    c2 = lps_recursive(startIdx, endIdx - 1)
                    dp[startIdx][endIdx] = max(c1, c2)
            return dp[startIdx][endIdx]
        return lps_recursive(0, len(s) - 1)
