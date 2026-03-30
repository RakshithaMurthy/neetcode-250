class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)  # Possible speed range is 1 to max pile size
        res = r  # Initialize result with upper bound

        while l <= r:
            k = l+ ((r-l) // 2)  # Try the middle speed

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / k)  # Total time for all piles at speed k

            if totalTime <= h:  # If she can eat all bananas within h hours
                res = k         # Update result to current k
                r = k - 1       # Try to find a smaller speed
            else:
                l = k + 1       # Try to find a higher speed
        return res