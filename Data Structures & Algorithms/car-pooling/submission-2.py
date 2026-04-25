class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x: x[1])

        heap =[]
        curr_pass = 0

        for num, start,end in trips:

            while heap and heap[0][0] <= start:
                e, n = heapq.heappop(heap)
                curr_pass -= n

            heapq.heappush(heap, (end, num))
            curr_pass += num

            if curr_pass > capacity:
                return False

        return True
        