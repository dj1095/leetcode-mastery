class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        dp = [[0] * (len(s2) + 1) for i in range(len(s1) + 1)]
        for i in range(len(s2)-1 , -1, -1):
            dp[len(s1)][i] = ord(s2[i]) +  dp[len(s1)][i + 1]
        for j in range(len(s1) - 1, -1, -1):
            dp[j][len(s2)] = ord(s1[j]) + dp[j + 1][len(s2)]

        for i in range(len(s1) - 1, -1, -1):
            for j in range(len(s2) -1, -1, -1):
                dp[i][j] = min(ord(s2[j]) + dp[i][j+1], ord(s1[i]) + dp[i+1][j]) if s1[i] != s2[j] else dp[i+1][j+1]
        
        print(dp)
        return dp[0][0]