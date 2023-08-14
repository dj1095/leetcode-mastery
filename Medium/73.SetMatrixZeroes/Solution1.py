class Solution:
    #### Not Optimal
    #Time Complexity - >O(M.N)
    #Space Complexity - O(M.N)

    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
        cpy = [matrix[r].copy() for r in range(rows)]

        def rowFill(row):
            nonlocal cpy
            for i in range(cols):
                cpy[row][i] = 0 

        def colFill(col):
            nonlocal cpy
            for i in range(rows):
                cpy[i][col] = 0 

        """
        Do not return anything, modify matrix in-place instead.
        """
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    rowFill(r)
                    colFill(c)
        print(cpy)
        return cpy