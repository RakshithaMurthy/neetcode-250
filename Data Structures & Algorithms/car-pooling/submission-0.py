from typing import List
import heapq

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        # Sort trips by start location
        trips.sort(key=lambda x: x[1])
        
        heap = []  # min-heap of (end, numPassengers)
        curr_passengers = 0
        
        for num, start, end in trips:
            
            # Drop off passengers whose trip ended before current start
            while heap and heap[0][0] <= start:
                e, n = heapq.heappop(heap)
                curr_passengers -= n
            
            # Pick up current passengers
            heapq.heappush(heap, (end, num))
            curr_passengers += num
            
            if curr_passengers > capacity:
                return False
        
        return True

        