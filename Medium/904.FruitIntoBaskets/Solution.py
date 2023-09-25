from collections import defaultdict
class Solution:
    # Time Complexity - O(N)
    #Space Complexity - O(1) since atmost we hold only two distinct tree type in the dictionary
    def totalFruit(self, fruits: List[int]) -> int:
        counts = defaultdict(int)
        max_length = 0
        no_of_baskets = 2
        start = 0
        for end in range(len(fruits)):
            counts[fruits[end]] += 1
            while len(counts) > no_of_baskets:
                if counts[fruits[start]] == 1:
                    counts.pop(fruits[start])
                else:
                    counts[fruits[start]] -= 1
                start += 1
            max_length = max(max_length , end - start + 1)
        return max_length
