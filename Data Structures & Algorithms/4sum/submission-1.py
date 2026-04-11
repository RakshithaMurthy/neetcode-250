from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                l, r = j + 1, n - 1

                while l < r:
                    total = nums[i] + nums[j] + nums[l] + nums[r]

                    if total == target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])

                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
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
k-sum

from typing import List

class Solution:
    def kSum(self, nums: List[int], target: int, k: int) -> List[List[int]]:
        nums.sort()

        def two_sum(start, target):
            res = []
            l, r = start, len(nums) - 1

            while l < r:
                total = nums[l] + nums[r]

                if total == target:
                    res.append([nums[l], nums[r]])

                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1

                    l += 1
                    r -= 1

                elif total < target:
                    l += 1
                else:
                    r -= 1

            return res

        def k_sum(start, target, k):
            res = []

            # base case
            if k == 2:
                return two_sum(start, target)

            for i in range(start, len(nums)):

                # skip duplicates
                if i > start and nums[i] == nums[i - 1]:
                    continue

                # recursive reduction
                subsets = k_sum(i + 1, target - nums[i], k - 1)

                for subset in subsets:
                    res.append([nums[i]] + subset)

            return res

        return k_sum(0, target, k)

'''