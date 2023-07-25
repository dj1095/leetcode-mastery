class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[float("inf")] * (len(word2) + 1) for i in range(len(word1) + 1)]
        for i in range(len(word2) + 1):
            dp[len(word1)][i] = len(word2) - i
        for j in range(len(word1) + 1):
            dp[j][len(word2)] = len(word1) - j
        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) -1, -1, -1):
                dp[i][j] = 1 + min(dp[i][j+1], dp[i+1][j]) if word1[i] != word2[j] else dp[i+1][j+1]
        return dp[0][0]