import heapq

class Solution:
    def findMaximizedCapital(self, k, w, profits, capital):
        
        projects = list(zip(capital, profits))
        projects.sort()  # sort by capital

        max_heap = []
        i = 0
        n = len(projects)

        for _ in range(k):

            # push all affordable projects
            while i < n and projects[i][0] <= w:
                heapq.heappush(max_heap, -projects[i][1])
                i += 1

            if not max_heap:
                break

            # pick most profitable
            w += -heapq.heappop(max_heap)

        return w