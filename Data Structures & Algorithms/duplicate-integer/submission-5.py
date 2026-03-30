class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        output =[]
        for i in range(n):
            if nums[i] not in output:
                output.append(nums[i])
            else:
                return True
        return False

        