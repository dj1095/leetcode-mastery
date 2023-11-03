class Solution:
    # Bottom Up Approach
    # Time and Space Complexity - O(N^2)
    def longestPalindromeSubseq(self, s: str) -> int:
        # Initialiazing DP Array
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]

        # every single letter is a palindrome
        for i in range(len(s)):
            dp[i][i] = 1

        for startIdx in range(len(s) - 1, -1, -1):
            for endIdx in range(startIdx + 1, len(s)):
                if s[startIdx] == s[endIdx]:
                    dp[startIdx][endIdx] = 2 + dp[startIdx + 1][endIdx - 1]
                else:
                    dp[startIdx][endIdx] = max(
                        dp[startIdx + 1][endIdx], dp[startIdx][endIdx - 1])
        return dp[0][len(s) - 1]
