class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        #Time Complexity - O(N)
        #Space Complexity - O(1)
        result = start = 0
        prev_matches = no_odd_nums = 0
        for end in range(len(nums)):
            if nums[end] % 2 == 1:
                no_odd_nums += 1
                #reset the cumulative matches when we encounter a odd number
                #because only non odd numbers need that cumulative sum
                prev_matches = 0
            #shrink the window when there is a match
            while no_odd_nums == k:
                prev_matches += 1
                if nums[start] % 2 == 1:
                    no_odd_nums -= 1
                start += 1
            result += prev_matches
        return result
