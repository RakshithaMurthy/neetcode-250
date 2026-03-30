class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        NumSet = set(nums)
        longest = 0

        for n in NumSet:
            if (n - 1) not in NumSet:
                length = 0
                while (n + length) in NumSet:
                    length += 1
                longest = max(length, longest)
        return longest