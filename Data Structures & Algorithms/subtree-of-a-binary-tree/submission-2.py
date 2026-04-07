# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same(p, q):
            if p and q and p.val == q.val:
                return same(p.left, q.left) and same(p.right, q.right)
            elif p or q:
                return False
            else:
                return True

        if root and subRoot:
            if same(root, subRoot):
                return True
            else:
                return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        elif subRoot:
            return False
        else:
            return True
