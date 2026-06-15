class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        # Build need map manually
        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1

        window = {}
        required = len(need)
        formed = 0

        left = 0
        min_len = float("inf")
        result = ""

        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c, 0) + 1

            # Check if this character just satisfied its requirement
            if c in need and window[c] == need[c]:
                formed += 1

            # Try shrinking the window
            while formed == required:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    result = s[left:right + 1]

                left_char = s[left]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    formed -= 1

                left += 1

        return result

'''
🔥 1. Minimum Window Substring (classic hard)
💡 Problem
Find smallest window in s that contains all characters of t.
🧠 Pattern
👉 Sliding window + frequency matching
We expand right, shrink left when valid.

🔥 2. Sliding Window Maximum
💡 Problem
Max element in every window of size k.
🧠 Pattern
👉 Monotonic decreasing deque

🔥 3. Sliding Window Minimum
💡 Same idea as max, but increasing deque
from collections import deque

class Solution:
    def minSlidingWindow(self, nums, k):
        dq = deque()
        res = []

        for i in range(len(nums)):
            while dq and nums[i] < nums[dq[-1]]:
                dq.pop()

            dq.append(i)

            if dq[0] <= i - k:
                dq.popleft()

            if i >= k - 1:
                res.append(nums[dq[0]])

        return res

Maintain increasing order → front is minimum

🔥 4. Sliding Window Median
💡 Problem
Median of each window of size k.
🧠 Pattern
👉 Two heaps (max heap + min heap)
Maintain two halves:
max heap = left side
min heap = right side


import heapq

class Solution:
    def medianSlidingWindow(self, nums, k):
        maxHeap = []  # lower half (negated)
        minHeap = []  # upper half
        res = []

        def add(num):
            heapq.heappush(maxHeap, -num)
            heapq.heappush(minHeap, -heapq.heappop(maxHeap))

            if len(minHeap) > len(maxHeap):
                heapq.heappush(maxHeap, -heapq.heappop(minHeap))

        def getMedian():
            if k % 2:
                return -maxHeap[0]
            return (-maxHeap[0] + minHeap[0]) / 2

        for i in range(len(nums)):
            add(nums[i])

            if i >= k:
                out = nums[i - k]
                if out in maxHeap:
                    maxHeap.remove(-out)
                    heapq.heapify(maxHeap)
                else:
                    minHeap.remove(out)
                    heapq.heapify(minHeap)

            if i >= k - 1:
                res.append(getMedian())

        return res

'''

#Sliding window + “what must be maintained efficiently?” decides the data structure.

