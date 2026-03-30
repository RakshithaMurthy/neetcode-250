class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictnums={}
        for i,j in enumerate(nums):
            diff = target - j
            if diff in dictnums:
                return [dictnums[diff], i]
            dictnums[j] = i
        return None

        