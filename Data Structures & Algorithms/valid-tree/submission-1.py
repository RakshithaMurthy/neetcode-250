from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        # Property 1: Tree must have exactly n-1 edges
        if len(edges) != n - 1:
            return False
        
        parent = list(range(n))
        rank = [0] * n
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # path compression
            return parent[x]
        
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            
            if rootX == rootY:
                return False  # cycle detected
            
            # Union by rank
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
                return False
        
        return True

        