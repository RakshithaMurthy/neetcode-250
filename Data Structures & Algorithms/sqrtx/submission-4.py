class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        l = 0
        r = x // 2

        while l < r:
            mid = (l + r + 1) // 2

            if mid * mid <= x:
                l = mid
            else:
                r = mid - 1

        return l