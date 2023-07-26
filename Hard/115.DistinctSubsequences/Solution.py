class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache = {}
        def dfs(sIdx , tIdx):
            if tIdx >= len(t):
                return 1
            elif sIdx >= len(s):
                return 0
            
            if (sIdx,tIdx) in cache:
                return cache[(sIdx , tIdx)]
            
            if s[sIdx] == t[tIdx]:
                cache[(sIdx , tIdx)] = dfs(sIdx + 1, tIdx + 1) + dfs(sIdx + 1, tIdx)
            else:
                cache[(sIdx , tIdx)] = dfs(sIdx + 1, tIdx)
            return cache[(sIdx , tIdx)]
        return dfs(0,0)

