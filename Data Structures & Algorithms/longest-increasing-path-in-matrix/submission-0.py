from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        if not matrix or not matrix[0]:
            return 0
        
        rows, cols = len(matrix), len(matrix[0])
        memo = [[0] * cols for _ in range(rows)]
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        def dfs(r, c):
            if memo[r][c] != 0:
                return memo[r][c]
            
            max_len = 1  # at least the cell itself
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < rows and 0 <= nc < cols:
                    if matrix[nr][nc] > matrix[r][c]:
                        max_len = max(max_len, 1 + dfs(nr, nc))
            
            memo[r][c] = max_len
            return max_len
        
        result = 0
        
        for r in range(rows):
            for c in range(cols):
                result = max(result, dfs(r, c))
        
        return result
