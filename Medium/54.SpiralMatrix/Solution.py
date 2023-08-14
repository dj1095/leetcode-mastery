class Solution:
    #Time Complexity - O(M.N)
    #Space Complexity - O(1)
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        left , right = 0, len(matrix[0])
        top , bottom = 0, len(matrix)

        while top < bottom and left < right:
             #iterate the top left to right
            for i in range(left, right):
                result.append(matrix[top][i])
            top += 1

            #iterate from  top right to bottom
            for i in range(top, bottom):
                result.append(matrix[i][right - 1])
            right -= 1

            if not (left < right and top < bottom):
                break

            #iterate bottom right to left
            for i in range(right - 1, left - 1, -1):
                result.append(matrix[bottom - 1][i])
            bottom -= 1

            #iterate from bottom left to top
            for i in range(bottom - 1, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
        return result
