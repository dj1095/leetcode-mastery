class Solution:
    #Bottom up approach
    #Time Complexity - O(amount * len(coins))
    #Space Complexity - O(amount)
    def coinChange(self, coins: List[int], amount: int) -> int:
        # to populate with max value in this case amount + 1
        dp = [amount + 1] * (amount + 1) 
        dp[0] = 0

        for amt in range(1,amount + 1) :
            for coin in coins:
                if amt - coin >=0:
                    dp[amt] = min(dp[amt], 1 + dp[amt - coin])
        return dp[amount] if dp[amount] != amount + 1 else -1

