class Solution:
    #Time complexity - O(N * logN) due to sorting
    #Space Complexity - O(N) due to space used by sorting otherwise O(1)
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : x[0])
        prevEnd = intervals[0][1]
        min_intervals = 0
        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                min_intervals += 1
                prevEnd = min(prevEnd, end)
        return min_intervals