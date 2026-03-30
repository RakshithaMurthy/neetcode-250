class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False

        target = total // k
        nums.sort(reverse=True)  # optimization
        used = [False] * len(nums)

        def backtrack(start, k, curr_sum):
            # all buckets filled
            if k == 0:
                return True

            # current bucket filled → move to next
            if curr_sum == target:
                return backtrack(0, k - 1, 0)

            for i in range(start, len(nums)):
                if used[i]:
                    continue

                if curr_sum + nums[i] > target:
                    continue

                # choose
                used[i] = True

                if backtrack(i + 1, k, curr_sum + nums[i]):
                    return True

                # backtrack
                used[i] = False

                # 🔥 pruning
                if curr_sum == 0:
                    break

            return False

        return backtrack(0, k, 0)

        