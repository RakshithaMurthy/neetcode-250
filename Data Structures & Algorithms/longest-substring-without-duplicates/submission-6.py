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

'''