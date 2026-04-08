# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def search(node, curr_max):
            if not node:
                return 0
            elif node.val >= curr_max:
                return 1 + search(node.left, node.val) + search(node.right, node.val)
            else:
                return search(node.left, curr_max) + search(node.right, curr_max)
        
        return search(root, float("-inf"))
