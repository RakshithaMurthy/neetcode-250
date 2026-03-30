class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_linear(houses):
            prev2 = 0
            prev1 = 0
            for money in houses:
                cur = max(prev1, prev2 + money)
                prev2 = prev1
                prev1 = cur
            return prev1

        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        # Two cases because houses are in a circle
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))
