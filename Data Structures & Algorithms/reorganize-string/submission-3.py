import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)

        # max heap (use negative freq)
        heap = [[-count, char] for char, count in freq.items()]
        heapq.heapify(heap)

        prev = None  # store previous char
        res = []

        while heap or prev:
            if prev and not heap:
                return ""  # no way to place remaining char

            count, char = heapq.heappop(heap)
            res.append(char)
            count += 1  # since negative

            # push previous back
            if prev:
                heapq.heappush(heap, prev)
                prev = None

            # if current still has count, hold it
            if count != 0:
                prev = [count, char]

        return "".join(res)