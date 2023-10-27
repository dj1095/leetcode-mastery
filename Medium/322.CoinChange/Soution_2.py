class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Time complexity - O(N * A)
        # Space Complexity - O(A)
        # the minimum number of coins to make up to amount is atleast amount number of 1 denoms
        dp = [0] + [amount + 1] * (amount)

        for i in range(len(coins)):
            for amt in range(coins[i], amount + 1):
                dp[amt] = min(dp[amt], 1 + dp[amt - coins[i]])

        return -1 if dp[amount] == amount + 1 else dp[amount]
