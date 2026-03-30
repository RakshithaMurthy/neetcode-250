class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = set()
        min_heap = [(0, 0)]  # (cost, node)
        total_cost = 0
        
        while len(visited) < n:
            cost, node = heapq.heappop(min_heap)
            
            if node in visited:
                continue
            
            visited.add(node)
            total_cost += cost
            
            for next_node in range(n):
                if next_node not in visited:
                    next_cost = abs(points[node][0] - points[next_node][0]) + \
                                abs(points[node][1] - points[next_node][1])
                    heapq.heappush(min_heap, (next_cost, next_node))
        
        return total_cost
