from typing import List

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        # Find the farthest drop-off point
        max_location = max(end for _, _, end in trips)
        
        # Initialize diff array
        diff = [0] * (max_location + 1)
        
        for num, start, end in trips:
            diff[start] += num
            diff[end] -= num
        
        # Prefix sum to check passengers
        curr = 0
        for p in diff:
            curr += p
            if curr > capacity:
                return False
        
        return True
