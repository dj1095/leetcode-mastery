class Solution:
    #Time Complexity - O(N + M) where N is len(s) and M is len(t)
    #Space Complexity - O(M) if we don't consider output string else O(N) if t is some permutation of s
    def minWindow(self, s: str, t: str) -> str:
        chr_freq_map = {}
        #Build a character frequency map
        for chr in t:
            if chr not in chr_freq_map:
                chr_freq_map[chr] = 0
            chr_freq_map[chr] += 1
        
        #Sliding Window Technique
        start = matched = 0
        sub_str_start = 0
        min_length = len(s) + 1 
        #Add to window till you find all characters in the window
        for end in range(len(s)):
            right_chr = s[end]
            if right_chr in chr_freq_map:
                chr_freq_map[right_chr] -= 1
                if chr_freq_map[right_chr] == 0:
                    matched += 1

            #Shrink window size once all characters are matched and check for min window that holds all chars
            while matched == len(chr_freq_map):
                left_chr = s[start]
                #update min length only when smaller window found
                if min_length > end - start + 1:
                    sub_str_start = start
                    min_length = end - start + 1
                start += 1
                if left_chr in chr_freq_map:
                    if chr_freq_map[left_chr] == 0:
                        matched -= 1
                    chr_freq_map[left_chr] += 1
               
        return "" if  min_length > len(s) else s[sub_str_start : sub_str_start + min_length]


        