class Solution:
    def findClosestElements(self, arr, k, x):
        l, r = 0, len(arr) - 1

        while r - l + 1 > k:
            if abs(arr[l] - x) > abs(arr[r] - x):
                l += 1
            else:
                r -= 1

        return arr[l:r+1]


'''
🔥 Step 1: What are we actually selecting?

We are asked for:

k closest elements to x

So final answer is:

a subset of size k
taken from a sorted array
also must remain sorted
💡 Key hidden insight

Because the array is sorted, the answer is NOT random.

👉 The k closest elements will always form a contiguous block (window) in the array.

🔥 Step 2: So problem becomes

Instead of:

pick k elements

We convert it to:

find the best window of size k

Think:

“I need k elements. I can remove elements from left or right.”

So we start with full array and shrink:

Two pointers version:
remove farthest element until size = k

🔥 Why that works

Because:

farthest element is least useful
removing it improves closeness
💡 Summary of thinking process

You don’t start with sliding window.

You arrive at it via:

Step 1:

We need k elements

Step 2:

Array is sorted → closest elements will cluster

Step 3:

Cluster = contiguous segment

Step 4:

So we search for best segment → sliding window

Because the array is sorted, the k closest elements must form a continuous block.”
'''
