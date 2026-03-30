"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

import heapq
from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        if not intervals:
            return 0
        
        # Sort by start time
        intervals.sort(key=lambda x: x.start)
        
        min_heap = []
        
        # Push end time of first meeting
        heapq.heappush(min_heap, intervals[0].end)
        
        for i in range(1, len(intervals)):
            start = intervals[i].start
            end = intervals[i].end
            
            # If earliest meeting finished
            if min_heap[0] <= start:
                heapq.heappop(min_heap)
            
            heapq.heappush(min_heap, end)
        
        return len(min_heap)
