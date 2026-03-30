from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        n = len(edges)
        parent = list(range(n + 1))  # nodes are 1-based
        rank = [0] * (n + 1)
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # path compression
            return parent[x]
        
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            
            if rootX == rootY:
                return False  # cycle detected
            
            # union by rank
            if rank[rootX] > rank[rootY]:
                parent[rootY] = rootX
            elif rank[rootX] < rank[rootY]:
                parent[rootX] = rootY
            else:
                parent[rootY] = rootX
                rank[rootX] += 1
            
            return True
        
        for u, v in edges:
            if not union(u, v):
                return [u, v]
        
        return []
