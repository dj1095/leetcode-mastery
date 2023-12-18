class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map1 = {}
        map2 = {}

        for i in range(len(s)):
            if s[i] not in map1 and t[i] not in map2:
                map1[s[i]] = t[i]
                map2[t[i]] = s[i]
            elif t[i] in map2 and map2[t[i]] == s[i]:
                continue
            else:
                return False
        return True
