class Solution:
    def mySqrt(self, x: int) -> int:
        #Time Complexity - O(logX) where X is the range of (0, x/2)
        #Space Complexity - O(1)

        # sqrt(x) can never be more that x/2 so right is taken below value
        right = x//2 + 1
        left = 0
        #performing binary Search 
        while left <= right:
            mid = left + ((right - left) // 2)
            prod = mid * mid
            if prod == x:
                return mid
            elif prod > x:
                right = mid - 1
            else:
                left = mid + 1
        #returning right boundary to give the closest integer to root
        return right
