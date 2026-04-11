class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        slow = 1

        for fast in range(1, len(nums)):
            if nums[fast] != nums[fast-1]:
                nums[slow] = nums[fast]
                slow+=1
        
        return slow


'''
#Allow 2 duplicates
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)

        slow = 2

        for fast in range(2, len(nums)):
            if nums[fast] != nums[slow - 2]:
                nums[slow] = nums[fast]
                slow += 1

        return slow

'''