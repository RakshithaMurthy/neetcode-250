"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        
        def build(r, c, size):
            # check if all values same
            val = grid[r][c]
            isLeaf = True

            for i in range(r, r + size):
                for j in range(c, c + size):
                    if grid[i][j] != val:
                        isLeaf = False
                        break
                if not isLeaf:
                    break

            # if same → leaf node
            if isLeaf:
                return Node(val, True, None, None, None, None)

            # otherwise split into 4 quadrants
            half = size // 2

            topLeft = build(r, c, half)
            topRight = build(r, c + half, half)
            bottomLeft = build(r + half, c, half)
            bottomRight = build(r + half, c + half, half)

            return Node(1, False, topLeft, topRight, bottomLeft, bottomRight)

        return build(0, 0, len(grid))

        