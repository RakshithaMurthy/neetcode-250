class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 2:
            return n

        def cmp(a, b):
            if a > b: return 1
            if a < b: return -1
            return 0

        l = 0
        res = 1

        for r in range(1, n):
            c = cmp(arr[r-1], arr[r])

            if c == 0:
                l = r
            elif r == 1 or c * cmp(arr[r-2], arr[r-1]) != -1:
                l = r - 1

            res = max(res, r - l + 1)

        return res
        