from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        left = 0
        curr_sum = 0
        min_len = float('inf')
        
        for right in range(len(nums)):
            curr_sum += nums[right]
            
            while curr_sum >= target:
                min_len = min(min_len, right - left + 1)
                curr_sum -= nums[left]
                left += 1
        
        return 0 if min_len == float('inf') else min_len

        
'''
1. Maximum sum subarray of size K (fixed window)
💡 Pattern: Fixed sliding window

class Solution:
    def maxSumSubarray(self, nums, k):
        l = 0
        window_sum = 0
        res = float('-inf')

        for r in range(len(nums)):
            window_sum += nums[r]

            if r - l + 1 > k:
                window_sum -= nums[l]
                l += 1

            if r - l + 1 == k:
                res = max(res, window_sum)

        return res

2. Average of subarrays of size K
💡 Same as above, just divide by k

class Solution:
    def findAverages(self, nums, k):
        l = 0
        window_sum = 0
        res = []

        for r in range(len(nums)):
            window_sum += nums[r]

            if r - l + 1 > k:
                window_sum -= nums[l]
                l += 1

            if r - l + 1 == k:
                res.append(window_sum / k)

        return res

3. Maximum sum subarray after at most one deletion
💡 Pattern: DP-like Kadane variant

We track:

keep element
delete one element
class Solution:
    def maximumSum(self, arr):
        n = len(arr)

        keep = arr[0]
        delete = 0
        res = arr[0]

        for i in range(1, n):
            delete = max(keep, delete + arr[i])
            keep = max(arr[i], keep + arr[i])

            res = max(res, keep, delete)

        return res

🔥 Intuition

At each index:

either continue subarray
or delete one element
5. Minimum sum subarray of size K
💡 Pattern: Fixed sliding window

class Solution:
    def minSumSubarray(self, nums, k):
        l = 0
        window_sum = 0
        res = float('inf')

        for r in range(len(nums)):
            window_sum += nums[r]

            if r - l + 1 > k:
                window_sum -= nums[l]
                l += 1

            if r - l + 1 == k:
                res = min(res, window_sum)

        return res

Fixed window → track sum, variable window → expand & shrink, deletion problems → DP-like state tracking

'''
