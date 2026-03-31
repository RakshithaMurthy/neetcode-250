from collections import defaultdict, deque

class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        
        def topo_sort(conditions):
            graph = defaultdict(list)
            indegree = [0] * (k + 1)

            for u, v in conditions:
                graph[u].append(v)
                indegree[v] += 1

            q = deque()
            for i in range(1, k + 1):
                if indegree[i] == 0:
                    q.append(i)

            order = []
            while q:
                node = q.popleft()
                order.append(node)
                for nei in graph[node]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        q.append(nei)

            return order if len(order) == k else []

        # Step 1: get row + col order
        row_order = topo_sort(rowConditions)
        col_order = topo_sort(colConditions)

        if not row_order or not col_order:
            return []

        # Step 2: map number → position
        row_pos = {num: i for i, num in enumerate(row_order)}
        col_pos = {num: j for j, num in enumerate(col_order)}

        # Step 3: build matrix
        res = [[0] * k for _ in range(k)]

        for num in range(1, k + 1):
            i = row_pos[num]
            j = col_pos[num]
            res[i][j] = num

        return res