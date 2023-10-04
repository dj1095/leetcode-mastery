class Solution:
    #Time Complexity - O(N)
    #Space Complexity - O(1)
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        result = start = 0
        sum = 0
        for end in range(len(arr)):
            sum += arr[end]
            if end >= k - 1 :
                if sum / k >= threshold:
                    result += 1
                sum -= arr[start]
                start += 1
        return result


        