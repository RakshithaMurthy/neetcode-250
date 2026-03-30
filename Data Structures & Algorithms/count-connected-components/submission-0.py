from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        parent = list(range(n))
        rank = [0] * n
        components = n
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # path compression
            return parent[x]
        
        def union(x, y):
            nonlocal components
            
            rootX = find(x)
            rootY = find(y)
            
            if rootX == rootY:
                return
            
            # union by rank
            if rank[rootX] > rank[rootY]:
                parent[rootY] = rootX
            elif rank[rootX] < rank[rootY]:
                parent[rootX] = rootY
            else:
                parent[rootY] = rootX
                rank[rootX] += 1
            
            components -= 1
        
        for u, v in edges:
            union(u, v)
        
        return components

        