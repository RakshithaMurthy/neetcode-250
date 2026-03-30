class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_linear(houses):
            n = len(houses)
            if n == 0:
                return 0
            if n == 1:
                return houses[0]

            dp = [0] * n
            dp[0] = houses[0]
            dp[1] = max(houses[0], houses[1])

            for i in range(2, n):
                dp[i] = max(dp[i-1], dp[i-2] + houses[i])

            return dp[-1]

        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        # Since houses are in a circle, consider two cases:
        # 1. Rob from 0 to n-2
        # 2. Rob from 1 to n-1
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))