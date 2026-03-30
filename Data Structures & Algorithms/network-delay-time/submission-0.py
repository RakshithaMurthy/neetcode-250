class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        
        # Build graph
        for u, v, w in times:
            graph[u].append((v, w))
        
        # Min-heap: (time, node)
        minHeap = [(0, k)]
        dist = {}
        
        while minHeap:
            time, node = heapq.heappop(minHeap)
            
            if node in dist:
                continue
            
            dist[node] = time
            
            for nei, w in graph[node]:
                if nei not in dist:
                    heapq.heappush(minHeap, (time + w, nei))
        
        # If not all nodes are reached
        if len(dist) != n:
            return -1
        
        return max(dist.values())
