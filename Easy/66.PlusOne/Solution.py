class Solution:
    ##AVOID!!!!****** Most Downvoted Question  
    #Time Complexity - O(N)
    #Space Complexity - O(N)
    def plusOne(self, digits: List[int]) -> List[int]:

        for i in range(len(digits)-1 , -1 , -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        return [1] + digits 

        