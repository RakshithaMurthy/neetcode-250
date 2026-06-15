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

'''
We maintain a structure that always keeps:

“Useful candidates for maximum in current window”

🔹 Why remove from back?
while nums[dq[-1]] < nums[i]:
    dq.pop()

Because:

smaller elements will NEVER be max again
current element dominates them
🔹 Why remove from front?
if dq[0] <= i - k:
    dq.popleft()

Because:

that index is out of current window
🔥 Key idea

Deque always holds:

indices of elements in decreasing order of value

So:
👉 front = max of window

🔥 Complexity
Type	Value
Time	O(n)
Space	O(k)
🔥 One-line intuition

“Keep a decreasing deque of useful elements for each sliding window.”

🔴 Why not simple loop?

Brute force:

O(nk)

Deque optimizes by ensuring:

each element enters and exits at most once

If you want, I can show a step-by-step animation of the deque movement, which makes this one of the most intuitive stack/deque problems.

what is the intuiton? how do I come up with deque for a sliding window problem?

Good question — this is exactly the “pattern recognition” jump people struggle with.

Let’s build the intuition from zero, not from code.

🔥 Step 1: What makes sliding window hard?

For each window of size k, you need:

“maximum element in that window”

Naive way:

scan all k elements every time → O(nk)

Problem:

too slow
repeated work every step
💡 Key observation

When the window moves:

[1, 3, -1] → [3, -1, -3]

Only TWO things happen:

one element leaves (left)
one new element enters (right)

👉 Most elements are still inside the window

🔥 Step 2: What do we really need?

We don’t need ALL elements.

We only need:

candidates that could become maximum

So ask:

❓ Which elements are useless?

If a new number comes in:

5 arrives when we already have 3

Then:

3 will NEVER be max again while 5 is in window
so we can discard 3 forever
🔥 Step 3: This is the key insight

We want to maintain:

“Only useful elements that can become maximum in future”

So we continuously remove:

smaller elements behind bigger ones
💡 This leads to structure:

We need:

fast add (right side)
fast remove (left side)
maintain order of importance

👉 That’s exactly what a deque gives

🔥 Step 4: Why deque specifically?

Because we need:

1. Remove from front (expired elements)
2. Remove from back (useless smaller elements)
3. Access max instantly (front)

Only deque supports all efficiently:

Operation	Deque
push back	O(1)
pop back	O(1)
pop front	O(1)
🔥 Step 5: The real mental model

Instead of thinking:

“I need max in window”

Think:

“Which elements are still worth keeping as candidates for max?”

🔥 Step 6: Why monotonic (decreasing) order?

We enforce:

big → small → smaller

Because:

bigger elements dominate smaller ones
smaller ones are useless while bigger exists

So:
👉 only decreasing structure survives

🔥 Step 7: Why does front give answer?

Because:

largest remaining candidate is always at front
everything behind is smaller

So:

dq[0] = max of window
🔥 Final intuition (MOST IMPORTANT)

You are not tracking the window.

You are tracking:

“a filtered list of only useful elements that could ever become maximum”

🔥 One-line mental model

“Keep only candidates for maximum, remove anything that can never win again.”

🔥 How to recognize deque problems in future

Use deque when you see:

✔ Sliding window + max/min
✔ Need “best in range”
✔ Repeated queries on overlapping ranges
✔ Brute force would re-scan same elements
🔥 Simple analogy

Think of it like a race:

every element is a runner
slower runners behind faster ones are removed
only strongest contenders remain
'''