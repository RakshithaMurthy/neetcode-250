from typing import List
import heapq
from collections import defaultdict

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], 
                          src: int, dst: int, k: int) -> int:
        
        # Build graph
        graph = defaultdict(list)
        for u, v, price in flights:
            graph[u].append((v, price))
        
        # Min heap: (cost, node, stops)
        heap = [(0, src, 0)]
        
        # To track best stops used to reach a node
        stops_record = {}
        
        while heap:
            cost, node, stops = heapq.heappop(heap)
            
            # If reached destination
            if node == dst:
                return cost
            
            # If stops exceed allowed, skip
            if stops > k:
                continue
            
            # If we've visited with fewer stops before, skip
            if (node in stops_record and 
                stops_record[node] <= stops):
                continue
            
            stops_record[node] = stops
            
            for neighbor, price in graph[node]:
                heapq.heappush(heap, 
                               (cost + price, neighbor, stops + 1))
        
        return -1
