class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        string = strs[0]
        resultStr = ""

        for idx in range(len(string)):
            for j in range(1,len(strs)):
                if idx >= len(strs[j]) or string[idx] != strs[j][idx]:
                    return resultStr
            resultStr += string[idx]

        return resultStr

            

ß