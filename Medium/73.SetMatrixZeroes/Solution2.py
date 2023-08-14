class Solution:
    #Better Solution but we can do constant space
    #Time Complexity - O(M.N)
    #Space Complexity - O(M + N)

    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
        rowChanges = [-1] * (rows) #O(M) space
        colChanges = [-1] * (cols) #O(N) space

        def rowFill(row):
            for i in range(cols):
                matrix[row][i] = 0 

        def colFill(col):
            for i in range(rows):
                matrix[i][col] = 0 

        """
        Do not return anything, modify matrix in-place instead.
        """
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    rowChanges[r] = r
                    colChanges[c] = c

        for r2 in rowChanges:
            if r2 >= 0:
                rowFill(r2)
        for c2 in colChanges:
            if c2 >= 0:
                colFill(c2)
