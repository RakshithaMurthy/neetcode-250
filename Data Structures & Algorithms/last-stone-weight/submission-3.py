class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
         #Convert to max-heap by using negative weights
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            # Pop two heaviest stones
            first = -heapq.heappop(stones)
            second = -heapq.heappop(stones)
            
            if first != second:
                # Push the difference back into heap
                heapq.heappush(stones, -(first - second))
        
        # Return the last stone or 0
        return -stones[0] if stones else 0