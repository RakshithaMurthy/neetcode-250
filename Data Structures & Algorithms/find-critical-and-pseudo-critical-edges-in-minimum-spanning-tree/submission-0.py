
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        self.parent[px] = py
        return True


def kruskal(n, edges, skip_edge=None, pick_edge=None):
    dsu = DSU(n)
    weight = 0

    # force include edge
    if pick_edge:
        u, v, w, _ = pick_edge
        if dsu.union(u, v):
            weight += w

    for u, v, w, i in edges:
        if i == skip_edge:
            continue

        if dsu.union(u, v):
            weight += w

    # check if all connected
    roots = set(dsu.find(i) for i in range(n))
    return weight if len(roots) == 1 else float('inf')


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        # add index
        edges = [edge + [i] for i, edge in enumerate(edges)]
        edges.sort(key=lambda x: x[2])

        # base MST weight
        base = kruskal(n, edges)

        critical = []
        pseudo = []

        for u, v, w, i in edges:

            # ❌ remove edge
            if kruskal(n, edges, skip_edge=i) > base:
                critical.append(i)

            # ✅ force include edge
            elif kruskal(n, edges, pick_edge=[u, v, w, i]) == base:
                pseudo.append(i)

        return [critical, pseudo]
