# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0

        def dfs(node, d):
            nonlocal max_depth
            if not node:
                return 

            max_depth = max(max_depth, d)

            dfs(node.left, d+1)
            dfs(node.right, d+1)

        dfs(root,1)
        return max_depth

            
        