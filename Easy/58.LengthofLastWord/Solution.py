class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        #Time Complexity - O(N)
        #Space Complexity - O(1)
        running_max = 0
        for i in range(len(s) - 1 , -1 , -1):
            if s[i] != ' ':
                running_max += 1
            elif running_max >0:
                return running_max
        return running_max
