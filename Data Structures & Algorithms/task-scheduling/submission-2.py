import heapq
from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks, n):
        freq = Counter(tasks)

        # max heap
        heap = [-cnt for cnt in freq.values()]
        heapq.heapify(heap)

        time = 0
        q = deque()  # (ready_time, count)

        while heap or q:
            time += 1

            if heap:
                cnt = heapq.heappop(heap)
                cnt += 1  # reduce count

                if cnt != 0:
                    q.append((time + n, cnt))

            # check if any task is ready
            if q and q[0][0] == time:
                heapq.heappush(heap, q.popleft()[1])

        return time