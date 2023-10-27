class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Time Complexity - O(N * A)
        # Space Complexity - O(N * A)
        # N = len(coins) and A = amount
        dp = [[float("inf") for _ in range(amount + 1)]
              for _ in range(len(coins))]

        # denominations needed to make sum 0
        for i in range(len(coins)):
            dp[i][0] = 0

        for i in range(len(coins)):
            for amt in range(1, amount + 1):
                if i > 0:
                    dp[i][amt] = dp[i - 1][amt]
                if amt >= coins[i]:
                    if dp[i][amt - coins[i]] >= 0:
                        dp[i][amt] = min(dp[i][amt], 1 + dp[i][amt - coins[i]])
        return -1 if dp[len(coins) - 1][amount] == float("inf") else dp[len(coins) - 1][amount]
