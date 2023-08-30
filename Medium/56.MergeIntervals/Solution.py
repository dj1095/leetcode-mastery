class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #Time Complexity - O(NlogN)
        #Space Complexity - O(N)
        #Both time and space are affected because of sorting logic
        intervals = sorted(intervals)
        
        result = [intervals[0]]
        for i in range(1, len(intervals)):
            #current start and end values
            s1 = intervals[i][0]
            e1 = intervals[i][1]
            #previously merged end value
            e0 = result[-1][1]

            if e0 >= s1:
                result[-1][1] = max(e0, e1)
            elif result[-1][1] < e1:
                result.append(intervals[i])
        return result

                


