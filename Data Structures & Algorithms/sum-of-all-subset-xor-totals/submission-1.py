class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.total = 0

        def dfs(i, curr_xor):
            if i == len(nums):
                self.total += curr_xor
                return

            # include
            dfs(i + 1, curr_xor ^ nums[i])

            # exclude
            dfs(i + 1, curr_xor)

        dfs(0, 0)
        return self.total
