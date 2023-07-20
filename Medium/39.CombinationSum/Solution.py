class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(idx, currentList, currentListTotal):
            if currentListTotal == target:
                res.append(currentList.copy())
                return
            if idx >= len(candidates) or currentListTotal > target:
                return
            currentList.append(candidates[idx])
            dfs(idx, currentList, currentListTotal + candidates[idx])
            currentList.pop()
            dfs(idx + 1, currentList, currentListTotal)

        dfs(0,[], 0)
        return res
            