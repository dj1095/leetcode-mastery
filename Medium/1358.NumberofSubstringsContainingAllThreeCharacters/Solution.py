class Solution:
    #Time Complexity - O(N)
    #Space Complexity - O(1)
    def numberOfSubstrings(self, s: str) -> int:
        result = prev_matches = start = 0
        counts = {}
        for end in range(len(s)):
            if s[end] not in counts:
                counts[s[end]] = 0
            counts[s[end]] += 1

            #After first match shrink the window to see number of matches in current window
            while len(counts) == 3:
                prev_matches += 1
                if counts[s[start]] == 1:
                    counts.pop(s[start])
                else:
                    counts[s[start]] -= 1
                start += 1
            # Cumulatively keep tracking of all matches[keep in mind once a previous match found it also contibutes to string in current window]
            result += prev_matches
        return result
            


