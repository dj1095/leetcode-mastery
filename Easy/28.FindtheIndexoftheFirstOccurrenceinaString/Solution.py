class Solution:
    #Time Complexity - O(N * K) ;N = len(haystack) and K = len(needle)
    #Space Complexity - O(1)
    def strStr(self, haystack: str, needle: str) -> int:
        for idx in range(len(haystack) - len(needle) + 1):
            if haystack[idx:idx + len(needle)] == needle:
                return idx
        return -1

        