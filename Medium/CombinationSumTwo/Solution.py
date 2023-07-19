class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(currentList, idx, listTotal):
            if listTotal == target:
                res.append(currentList.copy())
                return
            if listTotal > target:
                return 

            prev = -1
            for i in range(idx, len(candidates)):
                if prev == candidates[i]:
                    continue
                currentList.append(candidates[i])
                backtrack(currentList, i + 1, listTotal + candidates[i])
                currentList.pop()
                prev =  candidates[i]

        backtrack([], 0, 0)
        return res
       
                