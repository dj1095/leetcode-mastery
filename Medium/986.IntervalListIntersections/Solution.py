class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        #Time Complexity - O(N+M) - since iterating both lists once
        #Space Complexity - O(1) - ignoring the space required to store ouput else O(N + M)
        result = []
        i = 0
        j = 0
        while i < len(firstList) and j < len(secondList):
            first_overlaps_second = firstList[i][0] >= secondList[j][0] and firstList[i][0] <= secondList[j][1]
            second_overlaps_first = secondList[j][0] >= firstList[i][0] and secondList[j][0] <= firstList[i][1]
            if first_overlaps_second or second_overlaps_first:
                start = max(firstList[i][0] , secondList[j][0])
                end = min(firstList[i][1] , secondList[j][1])
                result.append([start, end])
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
        return result

        