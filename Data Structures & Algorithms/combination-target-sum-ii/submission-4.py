class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(start, path, total):
            if total == target:
                res.append(path[:])
                return
            if total > target:
                return

            for i in range(start, len(nums)):
                if i> start and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                backtrack(i+1, path, total + nums[i])  # reuse allowed
                path.pop()  # undo choice

        backtrack(0, [], 0)
        return res
        