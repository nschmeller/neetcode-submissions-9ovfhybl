# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def search(node, lower, upper):
            if not node:
                return True
            elif not lower < node.val < upper:
                return False
            else:
                return search(node.left, lower, node.val) and search(node.right, node.val, upper)
        
        return search(root, float("-inf"), float("inf"))
