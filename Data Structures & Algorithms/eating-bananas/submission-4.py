class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l= 1
        r = max(piles)

        while l < r:
            mid = (l+r)//2

            totaltime = 0
            for p in piles:
                totaltime += (math.ceil(float(p)/mid))

            if totaltime <= h:
                r = mid
            else:
                l = mid + 1

        return l
