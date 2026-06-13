class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix:
            return
        
        rows, cols = len(matrix), len(matrix[0])
        
        # prefix matrix with padding
        self.prefix = [[0] * (cols + 1) for _ in range(rows + 1)]

        for r in range(1, rows + 1):
            for c in range(1, cols + 1):
                self.prefix[r][c] = (
                    matrix[r-1][c-1]
                    + self.prefix[r-1][c]
                    + self.prefix[r][c-1]
                    - self.prefix[r-1][c-1]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.prefix[row2+1][col2+1]
            - self.prefix[row1][col2+1]
            - self.prefix[row2+1][col1]
            + self.prefix[row1][col1]
        )

#prefix[r][c] = sum of all elements from (0,0) to (r,c)
'''
🔹 1. Start with 1D prefix sum
Problem:

Fast range sum:

sum(l, r)
Build prefix:
prefix[i] = sum(nums[0] ... nums[i])

So:

prefix = [2, 5, 9, 12]

nums   = [2, 3, 4, 3]
🔥 Query idea:

To get sum(l → r):

prefix[r] - prefix[l-1]
Why?
prefix[r] → big sum
prefix[l-1] → remove left part

👉 This is “build once, subtract later”

🔹 2. Now extend idea to 2D

Instead of a line, we now have a grid:

a  b  c
d  e  f
g  h  i

We want:

sum of any submatrix

🔥 Key idea jump

In 1D:

prefix = sum from left

In 2D:

prefix[r][c] = sum of rectangle from (0,0) → (r,c)

So now prefix is:

top-left anchored rectangles
🔹 3. How to build 2D prefix (intuition)

At cell (r,c), you want:

everything above + everything left + current cell

But overlap is double counted:

So:
prefix[r][c] =
    up
  + left
  - overlap
  + current
🔥 Same structure as 1D, but in 2 directions
1D	2D
subtract left part	subtract top rectangle
simple line overlap	overlapping rectangle
🔹 4. The real bridge intuition
1D idea:

“I store cumulative sum up to i”

2D idea:

“I store cumulative sum up to (r,c) in both directions”

So instead of:

1D: grow right

you now:

2D: grow right AND down
🔥 5. How query becomes extension of 1D logic
1D query:
sum(l, r) = prefix[r] - prefix[l-1]
2D query:

You want rectangle:

(row1, col1) → (row2, col2)

So you do:

Step 1: take big rectangle
(0,0 → row2,col2)
Step 2: remove top
Step 3: remove left
Step 4: add overlap back
🔥 Final formula:
bottomRight
- top
- left
+ topLeftOverlap
'''
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)