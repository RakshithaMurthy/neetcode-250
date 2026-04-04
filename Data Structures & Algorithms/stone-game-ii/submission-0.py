from functools import lru_cache

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        # suffix sum
        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        @lru_cache(None)
        def dfs(i, M):
            if i >= n:
                return 0

            # take all remaining
            if i + 2*M >= n:
                return suffix[i]

            res = 0

            for x in range(1, 2*M + 1):
                res = max(res, suffix[i] - dfs(i + x, max(M, x)))

            return res

        return dfs(0, 1)