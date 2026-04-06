# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lca, found = root, False

        def hasAncestors(node):
            has_p = has_q = False
            if not node:
                return has_p, has_q
            elif node.val == p.val:
                has_p = True
            elif node.val == q.val:
                has_q = True

            has_p_left, has_q_left = hasAncestors(node.left)
            has_p_right, has_q_right = hasAncestors(node.right)

            has_p = has_p or has_p_left or has_p_right
            has_q = has_q or has_q_left or has_q_right

            nonlocal lca, found
            if not found and has_p and has_q:
                lca, found = node, True

            return has_p, has_q

        hasAncestors(root)
        return lca
