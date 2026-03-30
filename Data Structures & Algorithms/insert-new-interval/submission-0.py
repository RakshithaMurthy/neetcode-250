from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        result = []
        
        for interval in intervals:
            
            # case 1: interval before newInterval
            if interval[1] < newInterval[0]:
                result.append(interval)
            
            # case 2: interval after newInterval
            elif interval[0] > newInterval[1]:
                result.append(newInterval)
                newInterval = interval
            
            # case 3: overlap
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
        
        result.append(newInterval)
        
        return result
