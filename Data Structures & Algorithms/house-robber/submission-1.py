class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2 = 0
        prev1 = 0

        for money in nums:
            cur = max(prev1, prev2 + money)
            prev2 = prev1
            prev1 = cur

        return prev1


        

        