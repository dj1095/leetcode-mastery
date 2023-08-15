class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        #Time Complexity - O(S).O(26) = O(S)
        # Space Complexity - O(1)

        if len(p) > len(s):
            return []
        sCount , pCount = {} , {}
        for i in range(len(p)):
            pCount[p[i]] = 1 + pCount.get(p[i], 0)
            sCount[s[i]] = 1 + sCount.get(s[i], 0)

        result = [0] if pCount == sCount else []
        l = 0
        for r in range(len(p), len(s)):
            sCount[s[r]] = 1 + sCount.get(s[r],0)
            sCount[s[l]] -= 1
            if sCount[s[l]] == 0:
                sCount.pop(s[l])
            l += 1
            if sCount == pCount:
                result.append(l)
        return result
        