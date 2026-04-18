class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)

        def canship(cap):
            curr_load = 0
            day = 1

            for w in weights:
                if curr_load+w >cap:
                    day +=1
                    curr_load = 0
                curr_load +=w

            return day<=days

        while l < r:
            mid = (l+r)//2

            if canship(mid):
                r = mid
            else:
                l = mid+1

        return l
        