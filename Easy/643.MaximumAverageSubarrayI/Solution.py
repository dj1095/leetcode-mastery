class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        #Time Complexity - O(N)
        #Space Complexity - O(1)

        #sum of the first k elements
        initial_sum = sum(nums[:k])
        summ  = initial_sum
        running_sum = initial_sum

        #sliding Window
        for end in range(k, len(nums)):
            running_sum += nums[end] - nums[end - k]
            summ = max(summ , running_sum)
        return summ/k
        