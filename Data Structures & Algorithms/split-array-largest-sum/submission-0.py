class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def canSplit(max_sum):
            subarrays = 1
            curr_sum = 0

            for num in nums:
                curr_sum += num
                if curr_sum > max_sum:
                    subarrays += 1
                    curr_sum = num

            return subarrays <= k

        left, right = max(nums), sum(nums)

        while left < right:
            mid = (left + right) // 2

            if canSplit(mid):
                right = mid
            else:
                left = mid + 1

        return left

        