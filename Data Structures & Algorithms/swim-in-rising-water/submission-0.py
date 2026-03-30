from typing import List
import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        visited = set()
        
        # Min heap: (time, r, c)
        heap = [(grid[0][0], 0, 0)]
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        while heap:
            time, r, c = heapq.heappop(heap)
            
            if (r, c) in visited:
                continue
            
            visited.add((r, c))
            
            # If reached destination
            if r == n - 1 and c == n - 1:
                return time
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                    new_time = max(time, grid[nr][nc])
                    heapq.heappush(heap, (new_time, nr, nc))
        
        return -1
