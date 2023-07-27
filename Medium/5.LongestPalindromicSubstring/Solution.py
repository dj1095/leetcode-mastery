class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        #Time Complexity O(N^2)
        #Space Complexity O(1)
        lngstPal = ""
        for i in range(len(s)):
            lngstPal = max(lngstPal , self.getlongestPal(i, i, s), key=len)
            lngstPal = max(lngstPal , self.getlongestPal(i, i+1, s), key=len)
        return lngstPal

    def getlongestPal(self, leftIdx, rightIdx, s) :
        while leftIdx >=0 and rightIdx < len(s) and s[leftIdx] == s[rightIdx]:
            leftIdx -= 1
            rightIdx += 1
        return s[leftIdx+1: rightIdx]


        
