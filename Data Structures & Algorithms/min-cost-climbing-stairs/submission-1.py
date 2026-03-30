class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        #dp = [0] * (n)

        prev2 = cost[0]
        prev1 = cost[1]

        for i in range(2,n):
            #dp[i] = cost[i] + min(dp[i-1], dp[i-2])
            current = cost[i] + min(prev1, prev2)
            prev2 = prev1
            prev1 = current

        return min(prev2, prev1)
        