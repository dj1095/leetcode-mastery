class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(currentValue, currentList):
            if len(currentList) == k:
                res.append(currentList.copy())
                return 
            if currentValue > n or len(currentList) >= k :
                return 
            currentList.append(currentValue)
            dfs(currentValue + 1, currentList)
            currentList.pop()
            dfs(currentValue + 1, currentList)
        dfs(1, [])
        return res

            