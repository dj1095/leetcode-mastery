class Solution:
    #Time Complexity - O(N) 
    ## to find total distinct O(N) + outer loop O(N) + overall inner loop O(N) since we only see elements twice overall = O(N+N+N) = O(N)
    #Space Complexity - O(N)
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        start, result , previous_matches = 0, 0, 0
        # total distinct characters in the nums
        total_distinct = len(set(nums))
        freq = {}
        for end in range(len(nums)):
            if nums[end] not in freq:
                freq[nums[end]] = 0
            freq[nums[end]] += 1
            #shrink the window once a match is found
            while len(freq) == total_distinct:
                previous_matches += 1
                if freq[nums[start]] == 1:
                    freq.pop(nums[start])
                else:
                    freq[nums[start]] -= 1
                start += 1
            result += previous_matches
        return result
