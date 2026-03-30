class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = min_prod = res = nums[0]

        for num in nums[1:]:

            if num < 0:
                max_prod, min_prod = min_prod, max_prod

            max_prod = max(num, max_prod * num)
            min_prod = min(num, min_prod * num)

            res = max(res, max_prod)

        return res