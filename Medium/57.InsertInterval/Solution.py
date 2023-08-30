class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #Time Complexity - O(NlogN)
        #Space Complexity - O(1)
        #Both time and space are affected because of sorting logic
        intervals.append(newInterval)
        intervals.sort(key= lambda interval : interval[0])
        result = [intervals[0]]
        
        for start, end in intervals[1:]:
            if result[-1][1] >= start:
                result[-1][1] = max(result[-1][1] , end)
            elif result[-1][1] < end:
                result.append([start,end])
        return result