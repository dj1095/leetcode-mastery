class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        #Time Complexity - O(N^2) since there are almost  O(N* (N+1))/2 combinations we iterate
        #Space Complexity - O(N^2) if consider output
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1,1]]
        result  = [[1],[1,1]]
        for i in range(2, numRows):
            curr_list = [1]
            for j in range(1, i):
                curr_list.append(result[i - 1][j-1] + result[i - 1][j])
            curr_list.append(1)
            result.append(curr_list)
        return result
