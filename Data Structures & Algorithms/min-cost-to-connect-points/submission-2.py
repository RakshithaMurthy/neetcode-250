class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        
        visited = [False] * n
        minDist = [float('inf')] * n
        
        minDist[0] = 0   # Start from node 0
        total_cost = 0
        
        for _ in range(n):
            
            # 1. Pick unvisited node with smallest distance
            min_cost = float('inf')
            u = -1
            
            for i in range(n):
                if not visited[i] and minDist[i] < min_cost:
                    min_cost = minDist[i]
                    u = i
            
            # 2. Add to MST
            visited[u] = True
            total_cost += min_cost
            
            # 3. Update distances
            for v in range(n):
                if not visited[v]:
                    cost = abs(points[u][0] - points[v][0]) + \
                           abs(points[u][1] - points[v][1])
                    
                    if cost < minDist[v]:
                        minDist[v] = cost
        
        return total_cost
