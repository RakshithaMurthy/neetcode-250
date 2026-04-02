from collections import defaultdict, deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        if n == 1:
            return [0]

        graph = defaultdict(list)
        degree = [0] * n

        # build graph
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degree[u] += 1
            degree[v] += 1

        # initial leaves
        q = deque()
        for i in range(n):
            if degree[i] == 1:
                q.append(i)

        remaining = n

        # trim leaves
        while remaining > 2:
            size = len(q)
            remaining -= size

            for _ in range(size):
                leaf = q.popleft()
                for nei in graph[leaf]:
                    degree[nei] -= 1
                    if degree[nei] == 1:
                        q.append(nei)

        return list(q)