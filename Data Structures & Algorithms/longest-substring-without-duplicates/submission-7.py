class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res


'''
Subarrays with sum = K
Pattern: Prefix Sum + HashMap (NOT sliding window for negatives)
prefix_sum[i] = prefix_sum[j] - K
from collections import defaultdict

class Solution:
    def subarraySum(self, nums, k):
        freq = defaultdict(int)
        freq[0] = 1

        prefix = 0
        count = 0

        for num in nums:
            prefix += num

            count += freq[prefix - k]

            freq[prefix] += 1

        return count

#2. Subarrays with exactly K odd numbers
✔ Pattern: Sliding Window (At Most trick)
Key trick:
exactly K = atMost(K) - atMost(K-1)
class Solution:
    def numberOfSubarrays(self, nums, k):
        return self.atMost(nums, k) - self.atMost(nums, k - 1)

    def atMost(self, nums, k):
        l = 0
        count = 0
        res = 0

        for r in range(len(nums)):
            if nums[r] % 2 == 1:
                k -= 1

            while k < 0:
                if nums[l] % 2 == 1:
                    k += 1
                l += 1

            res += r - l + 1

        return res

#3. Subarrays with at most K distinct integers
from collections import defaultdict

class Solution:
    def subarraysWithKDistinct(self, nums, k):
        return self.atMost(nums, k) - self.atMost(nums, k - 1)

    def atMost(self, nums, k):
        freq = defaultdict(int)
        l = 0
        res = 0

        for r in range(len(nums)):
            freq[nums[r]] += 1

            while len(freq) > k:
                freq[nums[l]] -= 1
                if freq[nums[l]] == 0:
                    del freq[nums[l]]
                l += 1

            res += r - l + 1

        return res

4. Subarrays with product < K
class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        if k <= 1:
            return 0

        l = 0
        prod = 1
        res = 0

        for r in range(len(nums)):
            prod *= nums[r]

            while prod >= k:
                prod //= nums[l]
                l += 1

            res += r - l + 1

        return res
'''