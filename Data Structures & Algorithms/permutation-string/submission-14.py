class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        freq1 = [0] * 26
        freq2 = [0] * 26

    # Build frequency for s1 and first window of s2
        for i in range(len(s1)):
            freq1[ord(s1[i]) - ord('a')] += 1
            freq2[ord(s2[i]) - ord('a')] += 1

        if freq1 == freq2:
            return True

    # Slide the window
        left = 0
        for right in range(len(s1), len(s2)):
            freq2[ord(s2[right]) - ord('a')] += 1
            freq2[ord(s2[left]) - ord('a')] -= 1
            left += 1

            if freq1 == freq2:
                return True

        return False
        
'''
🔥 1. Fruit Into Baskets (At most 2 types)
💡 Problem
Longest subarray with at most 2 distinct elements
🧠 Pattern
👉 Sliding window + hashmap (at most K distinct)
Here K = 2
from collections import defaultdict

class Solution:
    def totalFruit(self, fruits):
        count = defaultdict(int)
        l = 0
        res = 0

        for r in range(len(fruits)):
            count[fruits[r]] += 1

            while len(count) > 2:
                count[fruits[l]] -= 1
                if count[fruits[l]] == 0:
                    del count[fruits[l]]
                l += 1

            res = max(res, r - l + 1)

        return res

🔥 2. Find All Anagrams in a String
💡 Problem
Find all start indices of substrings of s that are anagrams of p.
🧠 Pattern
👉 Fixed window + frequency match
Window size = len(p)
from collections import Counter

class Solution:
    def findAnagrams(self, s, p):
        need = Counter(p)
        window = Counter()

        l = 0
        res = []
        k = len(p)

        for r in range(len(s)):
            window[s[r]] += 1

            if r - l + 1 > k:
                window[s[l]] -= 1
                if window[s[l]] == 0:
                    del window[s[l]]
                l += 1

            if r - l + 1 == k and window == need:
                res.append(l)

        return res

. First Negative Number in Every Window of Size K
💡 Problem
For each window, return first negative number (or 0 if none)
🧠 Pattern
👉 Sliding window + queue (store indices)

from collections import deque

class Solution:
    def firstNegative(self, nums, k):
        dq = deque()
        res = []

        l = 0

        for r in range(len(nums)):
            if nums[r] < 0:
                dq.append(r)

            if r - l + 1 > k:
                if dq and dq[0] == l:
                    dq.popleft()
                l += 1

            if r - l + 1 == k:
                if dq:
                    res.append(nums[dq[0]])
                else:
                    res.append(0)

        return res

Sliding window problems differ only by what you store inside the window (freq map, deque, or counters).
'''

