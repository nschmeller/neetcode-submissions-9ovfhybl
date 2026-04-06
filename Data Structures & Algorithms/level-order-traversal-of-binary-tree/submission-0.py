# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict, deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        order, q = defaultdict(list), deque()
        if root:
            q.append((0, root))

        while q:
            level, node = q.popleft()
            order[level+1].append(node.val)
            
            if node.left:
                q.append((level+1, node.left))
            if node.right:
                q.append((level+1, node.right))

        return [order[level] for level in order]
