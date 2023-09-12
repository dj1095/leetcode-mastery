class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #Time Complexity - O(N) since the list is already sorted and we inserted and merged in linear time
        # Space Complexity - O(1) if we don't consider output array other wise O(N).
        idx = 0
        merged = []
        #Skip all the intervals that end before new Interval
        while  idx < len(intervals) and intervals[idx][1] < newInterval[0]:
            merged.append(intervals[idx])
            idx += 1
        
        #Merge all the overlapped intervals
        while idx < len(intervals) and intervals[idx][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[idx][0])
            newInterval[1] = max(newInterval[1], intervals[idx][1])
            idx += 1
        #Append the merged interval to the list
        merged.append(newInterval)

        #Append all remaining intervals as it is 
        while idx < len(intervals):
            merged.append(intervals[idx])
            idx += 1
        return merged