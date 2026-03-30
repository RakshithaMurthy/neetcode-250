# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        else:
            # CASE 1 & 2: one or zero child
            if not root.left:
                return root.right
            if not root.right:
                return root.left

            # CASE 3: two children
            # find inorder successor (smallest in right subtree)
            curr = root.right
            while curr.left:
                curr = curr.left

            # replace value
            root.val = curr.val

            # delete successor node
            root.right = self.deleteNode(root.right, curr.val)

        return root
