import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        
        projects = list(zip(capital, profits))
        projects.sort()  # sort by capital

        maxHeap = []
        i = 0
        n = len(projects)

        for _ in range(k):
            
            # add all affordable projects
            while i < n and projects[i][0] <= w:
                heapq.heappush(maxHeap, -projects[i][1])  # max heap
                i += 1

            if not maxHeap:
                break

            # pick most profitable
            w += -heapq.heappop(maxHeap)

        return w
