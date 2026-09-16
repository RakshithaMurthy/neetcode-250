import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks, n):

        freq =[0] * 26
        for task in tasks:
            freq[ord(task) - ord('A')] += 1

        heap =[]
        for f in freq:
            if f>0:
                heapq.heappush(heap, -f)

        time = 0
        q = deque()

        while heap or q:

            time +=1

            if heap:
                count = heapq.heappop(heap) + 1

                if count!=0:
                    q.append((count, time+n))

            if q and q[0][1] == time:
                heapq.heappush(heap,q.popleft()[0])

        return time



        