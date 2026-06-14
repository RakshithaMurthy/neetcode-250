from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        dq = deque()  # stores indices
        res = []

        for i in range(len(nums)):
            
            # 1. remove elements out of window
            if dq and dq[0] <= i - k:
                dq.popleft()

            # 2. remove smaller elements from back
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            dq.append(i)

            # 3. start adding results once first window is formed
            if i >= k - 1:
                res.append(nums[dq[0]])

        return res