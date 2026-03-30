# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Finding the Lowest Common Ancestor (LCA)

#The LCA of two nodes in a BST is defined as the deepest node that is an ancestor to both nodes. To find the LCA, we can use the properties of a BST:

    #If both p and q are less than the current node, then the LCA must be in the left subtree.
    #If both p and q are greater than the current node, then the LCA must be in the right subtree.
    #If one of p or q is equal to the current node, or if one is on one side and the other is on the opposite side, then the current node is the LCA.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or not p or not q:
            return None
        if (max(p.val, q.val) < root.val):
            return self.lowestCommonAncestor(root.left, p, q)
        elif (min(p.val, q.val) > root.val):
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root