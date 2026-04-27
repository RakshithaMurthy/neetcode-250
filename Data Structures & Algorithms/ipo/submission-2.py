import heapq

class Solution:
    def findMaximizedCapital(self, k, w, profits, capital):

        projects = list(zip(capital, profits))
        projects.sort()   # sort by required capital

        heap = []
        i = 0
        n = len(projects)

        for _ in range(k):

            # add all affordable projects
            while i < n and projects[i][0] <= w:
                heapq.heappush(heap, -projects[i][1])   # max heap
                i += 1

            # no available project
            if not heap:
                break

            # choose most profitable project
            w += -heapq.heappop(heap)

        return w