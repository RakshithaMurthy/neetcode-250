class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = min_prod = ans = nums[0]

        for num in nums[1:]:
            prev_max = max_prod
            prev_min = min_prod

            max_prod = max(num, num * prev_max, num * prev_min)

            min_prod = min(num, num * prev_max, num * prev_min)

            ans = max(ans, max_prod)

        return ans
