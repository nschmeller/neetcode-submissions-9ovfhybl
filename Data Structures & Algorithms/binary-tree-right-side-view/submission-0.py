# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res, q = [], deque([(root, 0)])
        while q:
            curr, level = q.popleft()
            if not q or q[0][1] > level:
                res.append(curr.val)
            
            if curr.left:
                q.append((curr.left, level+1))
            if curr.right:
                q.append((curr.right, level+1))
        
        return res
