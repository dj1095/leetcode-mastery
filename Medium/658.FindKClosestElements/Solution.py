class Solution:
    #Time Complexity - O(N)
    #Space Complexity - O(1)
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        start , end = 0 , len(arr) - 1
        while end - start + 1 > k:
            if abs(x - arr[start]) > abs(x - arr[end]):
                start += 1
            else:
                end -= 1
        return arr[start: end + 1]
