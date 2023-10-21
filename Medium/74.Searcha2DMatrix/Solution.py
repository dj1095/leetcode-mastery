class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Time Complexity - O(log(M * N))
        # Space Complexity - O(1)
        if not matrix or not matrix[0]:
            return False

        rows, cols = len(matrix), len(matrix[0])

        def binary_search():
            left, right = 0, rows * cols - 1
            while left <= right:
                mid = (right + left) // 2
                mid_row, mid_col = mid // cols, mid % cols
                if matrix[mid_row][mid_col] == target:
                    return True
                elif matrix[mid_row][mid_col] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return False

        return binary_search()
