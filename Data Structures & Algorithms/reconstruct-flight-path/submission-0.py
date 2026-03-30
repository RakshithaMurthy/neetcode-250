from typing import List
from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        graph = defaultdict(list)
        
        # Sort tickets in reverse lexicographical order
        for src, dst in sorted(tickets, reverse=True):
            graph[src].append(dst)
        
        result = []
        
        def dfs(airport):
            while graph[airport]:
                next_airport = graph[airport].pop()
                dfs(next_airport)
            result.append(airport)
        
        dfs("JFK")
        
        return result[::-1]
