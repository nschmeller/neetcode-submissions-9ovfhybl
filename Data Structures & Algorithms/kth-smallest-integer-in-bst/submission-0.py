# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        remaining = k
        found = -1

        def inorder(node):
            nonlocal remaining, found
            if node:
                inorder(node.left)
                remaining -= 1
                if remaining == 0:
                    found = node.val
                inorder(node.right)
        
        inorder(root)
        return found
