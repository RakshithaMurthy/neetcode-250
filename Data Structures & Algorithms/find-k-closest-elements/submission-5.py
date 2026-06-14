from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        left = 0
        right = len(arr) - k
        
        while left < right:
            mid = (left + right) // 2
            
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        
        return arr[left:left + k]


'''
l, r = 0, len(arr) - k
💡 Why?

We are choosing the starting index of a window of size k.

If array length = n
last valid start index = n - k

So:

window = arr[i : i+k]
i ∈ [0, n-k]

👉 That’s why search range is [0, n-k]

🔥 Next line
while l < r:
💡 Why?

We are doing binary search on window start index

We are narrowing down:

“Which window of size k is best?”

🔥 Mid calculation
m = (l + r) // 2
💡 Why?

We are testing a candidate window starting at m.

🔥 Core comparison
if x - arr[m] > arr[m + k] - x:

This is the MOST IMPORTANT line.

💡 What are we comparing?

We compare two possible windows:

Window 1 starts at m:
arr[m ... m+k-1]
We decide if we should shift right.
🔹 Compare boundary elements:
Expression	Meaning
arr[m]	left edge of window
arr[m+k]	element just outside right edge
💡 Interpretation:
distance of left edge to x
vs
distance of right outside element to x
🔥 Why this tells direction?

We ask:

“Should this window move right?”

If:

left side is farther from x than right outside element

👉 window should shift right

So:

l = m + 1
🔥 Else case
else:
    r = m
💡 Meaning:
current window is good or better
try smaller (left side)
🔥 Why shrinking works

Because:

better windows cluster
we eliminate half search space each time

So we can binary search over windows

🔥 Final return
return arr[l:l + k]
💡 Why?

At the end:

l = best starting index of window
so return that window of size k
🔥 Full intuition (VERY IMPORTANT)

We are NOT selecting elements.

We are selecting:

a sliding block of size k in a sorted array

🔥 One-line mental model

“Binary search the best window of size k by comparing which side is farther from x.”

🔥 Why this works (deep intuition)

Because:

as window moves right → values increase
closeness changes smoothly (monotonic trend)

So:
👉 valid for binary search

✔ Summary
Line	Meaning
l, r = 0, n-k	search window start index
m = ...	try middle window
compare edges	decide shift direction
l = m+1	move right
r = m	move left
return slice	final best window
'''
