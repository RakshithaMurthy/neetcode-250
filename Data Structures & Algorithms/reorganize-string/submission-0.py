import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        
        # max heap
        heap = [(-freq, ch) for ch, freq in count.items()]
        heapq.heapify(heap)

        res = []

        while len(heap) >= 2:
            f1, c1 = heapq.heappop(heap)
            f2, c2 = heapq.heappop(heap)

            res.append(c1)
            res.append(c2)

            if f1 + 1 < 0:
                heapq.heappush(heap, (f1 + 1, c1))
            if f2 + 1 < 0:
                heapq.heappush(heap, (f2 + 1, c2))

        # handle last char
        if heap:
            f, c = heapq.heappop(heap)
            if f < -1:
                return ""
            res.append(c)

        return "".join(res)

        