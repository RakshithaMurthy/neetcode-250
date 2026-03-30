class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n = len(matrix), len(matrix[0])
        left, right = 0, (m*n -1)

        while left<=right:
            mid = (left +right) // 2
            mid_value = matrix[mid // n][mid % n]

            if mid_value == target:
                return True
            elif mid_value < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False


#// n gives the row index because each row contains n elements, and integer division tells you how many complete rows fit into the index.
# % n gives the column index because it tells you the position within the current row, effectively resetting after every n elements.
