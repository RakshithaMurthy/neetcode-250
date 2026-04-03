import heapq

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        
        meetings.sort()
        
        available = list(range(n))  # all rooms free
        heapq.heapify(available)
        
        occupied = []  # (end_time, room)
        
        count = [0] * n
        
        for start, end in meetings:
            
            # free rooms
            while occupied and occupied[0][0] <= start:
                _, room = heapq.heappop(occupied)
                heapq.heappush(available, room)
            
            duration = end - start
            
            if available:
                room = heapq.heappop(available)
                heapq.heappush(occupied, (end, room))
            else:
                end_time, room = heapq.heappop(occupied)
                heapq.heappush(occupied, (end_time + duration, room))
            
            count[room] += 1
        
        # return room with max count (smallest index if tie)
        return count.index(max(count))