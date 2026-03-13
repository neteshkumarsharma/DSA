class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i, j = 0, len(matrix[0]) - 1
        n = len(matrix) - 1
        while i <= n and j >= 0:
            if matrix[i][j] == target:
                return True
            if target < matrix[i][j]:
                j -= 1
            else:
                i += 1
        return False