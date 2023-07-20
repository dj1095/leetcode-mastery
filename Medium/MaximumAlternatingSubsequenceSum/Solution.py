class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        #DP Approach 
        evenSum , oddSum = 0,0

        for num in nums:
            tempEven = max( oddSum + num , evenSum)
            tempOdd = max(evenSum - num , oddSum)
            evenSum, oddSum = tempEven, tempOdd
        return evenSum
            


    