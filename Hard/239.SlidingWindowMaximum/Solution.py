from collections import deque;
class Solution:
    #Time Complexity - O(N)
    #Space Complexity - O(K) - if we consider only queue space . O(N) if we consider output space in worst case
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        start = 0
        output = []
        max_q = deque()
        for end in range(len(nums)):
            #pop all elements from deque that less than the current element
            while max_q and nums[max_q[-1]] < nums[end]:
                max_q.pop()
            #Add index to the deque
            max_q.append(end)
            # Pop the max element if it is going out of window 
            if end >= k - 1:
                output.append(nums[max_q[0]])
                if start == max_q[0]:
                    max_q.popleft()
                start += 1
        return output
            



            

        