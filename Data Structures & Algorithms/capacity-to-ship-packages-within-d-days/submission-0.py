from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def canShip(capacity):
            days_needed = 1
            curr_load = 0
            
            for w in weights:
                if curr_load + w > capacity:
                    days_needed += 1
                    curr_load = 0
                curr_load += w
            
            return days_needed <= days
        
        left = max(weights)
        right = sum(weights)
        
        while left < right:
            mid = (left + right) // 2
            
            if canShip(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
