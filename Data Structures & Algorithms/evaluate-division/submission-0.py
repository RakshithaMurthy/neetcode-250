from collections import defaultdict

class Solution:
    def calcEquation(self, equations, values, queries):
        
        graph = defaultdict(list)

        # Step 1: build graph
        for (a, b), val in zip(equations, values):
            graph[a].append((b, val))
            graph[b].append((a, 1 / val))

        # Step 2: DFS
        def dfs(src, target, visited):
            if src not in graph:
                return -1.0
            if src == target:
                return 1.0

            visited.add(src)

            for nei, weight in graph[src]:
                if nei not in visited:
                    res = dfs(nei, target, visited)
                    if res != -1:
                        return res * weight

            return -1.0

        # Step 3: process queries
        res = []
        for a, b in queries:
            res.append(dfs(a, b, set()))

        return res