from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        prefix_count = defaultdict(int)
        prefix_count[0] = 1
        
        prefix_sum = 0
        count = 0
        
        for num in nums:
            prefix_sum += num
            #count += number of times (prefix_sum - k) appeared before
            if prefix_sum - k in prefix_count:
                count += prefix_count[prefix_sum - k]
            
            prefix_count[prefix_sum] += 1
        
        return count

'''
🔥 1. Longest subarray with sum ≤ target (POSITIVE numbers)
💡 Pattern: Classic sliding window

Because numbers are positive → sum is monotonic.

class Solution:
    def longestSubarray(self, nums, target):
        l = 0
        s = 0
        res = 0

        for r in range(len(nums)):
            s += nums[r]

            while s > target:
                s -= nums[l]
                l += 1

            res = max(res, r - l + 1)

        return res


2. Longest subarray with absolute difference ≤ limit
💡 Pattern: Sliding window + monotonic deques

We need:

max - min ≤ limit
\from collections import deque

class Solution:
    def longestSubarray(self, nums, limit):
        maxdq = deque()
        mindq = deque()

        l = 0
        res = 0

        for r in range(len(nums)):
            # maintain max deque
            while maxdq and nums[r] > maxdq[-1]:
                maxdq.pop()
            maxdq.append(nums[r])

            # maintain min deque
            while mindq and nums[r] < mindq[-1]:
                mindq.pop()
            mindq.append(nums[r])

            # shrink if invalid
            while maxdq[0] - mindq[0] > limit:
                if nums[l] == maxdq[0]:
                    maxdq.popleft()
                if nums[l] == mindq[0]:
                    mindq.popleft()
                l += 1

            res = max(res, r - l + 1)

        return res

3. Shortest subarray with sum ≥ S
💡 Pattern: Sliding window (ONLY positive numbers)

We shrink aggressively to minimize size.

class Solution:
    def minSubArrayLen(self, target, nums):
        l = 0
        s = 0
        res = float('inf')

        for r in range(len(nums)):
            s += nums[r]

            while s >= target:
                res = min(res, r - l + 1)
                s -= nums[l]
                l += 1

        return 0 if res == float('inf') else res

4. 4. Longest subarray with at most K zeros
💡 Pattern: Sliding window (binary constraint)

class Solution:
    def longestOnes(self, nums, k):
        l = 0
        res = 0
        zeros = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                zeros += 1

            while zeros > k:
                if nums[l] == 0:
                    zeros -= 1
                l += 1

            res = max(res, r - l + 1)

        return res

If constraint is monotonic → sliding window works; if you need max/min in window → use deque.

'''