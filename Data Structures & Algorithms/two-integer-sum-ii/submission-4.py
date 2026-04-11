class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l,r = 0, len(numbers) - 1

        while l<r:
            cursum = numbers[l] + numbers[r]

            if cursum>target:
                r-=1
            elif cursum< target:
                l+=1
            else:
                return[l+1, r+1]
        return []  
            

'''
Skip duplicates

from typing import List

class Solution:
    def twoSumUnique(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        l, r = 0, len(nums) - 1

        while l < r:
            total = nums[l] + nums[r]

            if total == target:
                res.append([nums[l], nums[r]])

                # skip duplicates on left
                while l < r and nums[l] == nums[l + 1]:
                    l += 1

                # skip duplicates on right
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1

                l += 1
                r -= 1

            elif total < target:
                l += 1
            else:
                r -= 1

        return res

'''