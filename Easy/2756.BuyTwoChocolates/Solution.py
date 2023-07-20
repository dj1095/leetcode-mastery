class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        minimumSum= self.getSmallestValues(prices)
        purchaseValue = money - minimumSum
        return purchaseValue if purchaseValue >=0 else money


    #Find the minimum sum from two values 
    def getSmallestValues(self,prices):
        smallest = min(prices[0],prices[1])
        secondSmallest = max(prices[0],prices[1])
        for idx in range(2,len(prices)):
            if prices[idx] < smallest:
                secondSmallest = smallest
                smallest = prices[idx]
            elif prices[idx] >= smallest and prices[idx] < secondSmallest:
                secondSmallest = prices[idx]
        return smallest + secondSmallest
            



            