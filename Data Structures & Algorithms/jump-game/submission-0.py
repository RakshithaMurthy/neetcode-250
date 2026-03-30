class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #n = len(nums)

        #dp = [False] * n

        #dp[i] = nums[i], dp[i-1]

        goal = len(nums) - 1
        for i in range(len(nums) - 2, -1,-1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0

        