class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1  # Treat the matrix as a 1D array

        while left <= right:
            mid = (left + right) // 2
            mid_value = matrix[mid // n][mid % n]  # Convert mid to 2D indices
            
            if mid_value == target:
                return True
            elif mid_value < target:
                left = mid + 1
            else:
                right = mid - 1

        return False