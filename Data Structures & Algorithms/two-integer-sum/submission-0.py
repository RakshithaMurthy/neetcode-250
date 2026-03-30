class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        archivemap ={}

        for i, j in enumerate(nums):
            diff = target - j
            if diff in archivemap:
                return [archivemap[diff], i]
            archivemap[j] = i
        return
        