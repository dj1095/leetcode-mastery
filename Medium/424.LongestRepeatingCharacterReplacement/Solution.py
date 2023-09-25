from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #Time Complexity - O(N)
        ### Space Complexity - O(1) . 
        ###As we expect only the lower case letters in the input string, 
        ### we can conclude that the space complexity will be O(26) 
        ### to store each letter’s frequency in the HashMap, which is asymptotically equal to O(1).
        start  = 0
        max_len = max_repeating_char_count = 0
        counts = defaultdict(int)
        for end in range(len(s)):
            counts[s[end]] += 1
            max_repeating_char_count = max(max_repeating_char_count , counts[s[end]])

            if (end - start + 1) - max_repeating_char_count > k:
                counts[s[start]] -= 1
                start += 1
            max_len = max(max_len, end - start + 1)
        return max_len
