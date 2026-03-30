class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_arr = set(nums)
        return True if len(set_arr) != len(nums) else False
        