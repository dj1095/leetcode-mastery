class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        #Time and Space O(M * N)
        # M - Total number of coins or len(coins)
        # N - Amount to be sum 
        cache = {}
        def dfs(currentAmt, i):
            if currentAmt == amount:
                return 1
            if currentAmt > amount or i == len(coins):
                return 0
            if (currentAmt, i) in cache:
                return cache[(currentAmt, i)]
            
            cache[(currentAmt, i)] = dfs(currentAmt+coins[i], i) + dfs(currentAmt, i+1)
            return cache[(currentAmt, i)]
        
        return dfs(0,0)