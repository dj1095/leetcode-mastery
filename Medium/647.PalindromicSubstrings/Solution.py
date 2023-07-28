class Solution:
    def countSubstrings(self, s: str) -> int:
         #Time Complexity O(N^2)
        #Space Complexity O(1)
        palindromeSubstrCount = 0
        for i in range(len(s)):
            palindromeSubstrCount += self.getlongestPal(i, i, s)
            palindromeSubstrCount += self.getlongestPal(i, i+1, s)
        return palindromeSubstrCount

    def getlongestPal(self, leftIdx, rightIdx, s) :
        count = 0
        while leftIdx >=0 and rightIdx < len(s) and s[leftIdx] == s[rightIdx]:
            leftIdx -= 1
            rightIdx += 1
            count += 1
        return count